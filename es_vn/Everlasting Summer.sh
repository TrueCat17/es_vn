#!/bin/sh

if [ "`uname -s`" = "Darwin" ]; then
	echo "MacOS is not supported now"
	exit 1
fi

file_path=`realpath "$0"`
dir_path=`dirname "$file_path"`

case "`uname -m`" in
	x86_64|amd64)
		exec "$dir_path/Ren-Engine/linux-x86_64"
		;;
	i*86)
		exec "$dir_path/Ren-Engine/linux-i686"
		;;
	*)
		echo "Unknown architecture"
		echo "You can run need file in dir Ren-Engine"
		exit 1
		;;
esac
