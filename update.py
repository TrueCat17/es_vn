#!/usr/bin/env -S python3 -B
import os
import hashlib
import time

def error(msg):
	print(msg)
	os.sys.exit(1)

def get_hash(content):
	h = hashlib.new('sha256')
	h.update(content)
	return h.hexdigest()


dir = os.path.dirname(os.path.abspath(__file__).replace('\\', '/')) + '/'
zips_path = dir + 'zips/'
files_path = dir + 'files/'
info_path = dir + 'info.txt'
version_path = dir + 'version.txt'

os.makedirs(files_path, exist_ok = True)
os.makedirs(zips_path, exist_ok = True)


def get_zip():
	zn = None
	zn_mtime = 0
	for fn in os.listdir(zips_path):
		if fn.endswith('.zip'):
			fn = zips_path + fn
			mtime = os.stat(fn).st_mtime
			if mtime > zn_mtime:
				mtime = zn_mtime
				zn = fn
	if not zn:
		error('Zip file in <zips> was not found')
	
	print('Last created zip:', zn)
	
	import zipfile
	zf = zipfile.ZipFile(zn, 'r')
	dirs, files = set(), set()
	
	for fn in zf.namelist():
		container = dirs if fn.endswith('/') else files
		container.add(fn)
		
		# zip can contains a/b/c.txt without a/ and a/b/
		# fix it
		while True:
			index = fn.rfind('/', 0, -1)
			if index == -1:
				break
			fn = fn[0:index + 1]
			dirs.add(fn)
	
	return zf, dirs, files

def get_current_files():
	dirs, files = set(), set()
	
	def join(a, b, suffix):
		if a:
			return a + '/' + b + suffix
		return b + suffix
	
	for p, ds, fs in os.walk(files_path):
		p = p[len(files_path):]
		for i in ds:
			dirs.add(join(p, i, '/'))
		for i in fs:
			files.add(join(p, i, ''))
	
	return dirs, files


def set_version():
	formatted = time.strftime('%Y.%m.%d-%H:%M:%S')
	with open(version_path, 'wb') as f:
		f.write(formatted.encode('utf-8'))


def content_read():
	global hashes, sizes, was_updated
	hashes = {}
	sizes = {}
	was_updated = False
	
	if not os.path.exists(info_path):
		return
	
	with open(info_path, 'rb') as f:
		content = f.read().decode('utf-8')
	for s in content.split('\n'):
		if s:
			fn, hash, size = s.split('|')
			hashes[fn] = hash
			sizes[fn] = size

def content_write():
	if was_updated:
		with open(info_path, 'wb') as f:
			for fn in sorted(hashes.keys()):
				s = '%s|%s|%s\n' % (fn, hashes[fn], sizes[fn])
				f.write(s.encode('utf-8'))
		set_version()
	else:
		print('No changes')

def content_add(fn, new_content = None):
	global was_updated
	was_updated = True
	
	full_path = files_path + fn
	if os.path.exists(full_path):
		print(' *upd:', fn)
	else:
		print(' +add:', fn)
	
	if new_content is None:
		if fn[-1] != '/':
			error('<new_content> is None for file <%s>' % fn) # internal error
		os.makedirs(full_path, exist_ok = True)
		hashes[fn] = ''
		sizes[fn] = '0'
	else:
		with open(full_path, 'wb') as f:
			f.write(new_content)
		hashes[fn] = get_hash(new_content)
		sizes[fn] = str(len(new_content))

def content_remove(fn):
	global was_updated
	was_updated = True
	
	print(' -rm:', fn)
	
	hashes[fn] = ''
	sizes[fn] = ''
	remove = os.rmdir if fn.endswith('/') else os.remove
	remove(files_path + fn)


def main():
	content_read()
	
	zip_file, zip_dirs, zip_files = get_zip()
	cur_dirs, cur_files = get_current_files()
	
	prefix = min(zip_dirs) # project_name/
	prefix_len = len(prefix)
	
	for i in zip_dirs | zip_files:
		if not i.startswith(prefix):
			error('Zip has more than one root')
	
	zip_dirs = set(i[prefix_len:] for i in zip_dirs if i != prefix)
	zip_files = set(i[prefix_len:] for i in zip_files)
	
	for d in zip_dirs - cur_dirs:
		if not d.startswith('var/'):
			content_add(d)
	
	for fn in cur_files:
		if fn not in zip_files:
			content_remove(fn)
			continue
		
		with open(files_path + fn, 'rb') as cur_file:
			cur_file_content = cur_file.read()
		
		with zip_file.open(prefix + fn) as next_file:
			next_file_content = next_file.read()
		
		if cur_file_content != next_file_content:
			content_add(fn, next_file_content)
	
	for zip_fn in zip_files:
		if zip_fn.startswith('var/'): continue
		if zip_fn in cur_files: continue
		
		with zip_file.open(prefix + zip_fn) as next_file:
			next_file_content = next_file.read()
		content_add(zip_fn, next_file_content)
	
	# sort to remove a/b/ before a/
	for d in sorted(cur_dirs - zip_dirs, reverse = True):
		content_remove(d)
	
	content_write()

main()
