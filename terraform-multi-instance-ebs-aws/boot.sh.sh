#!/bin/bash

sleep 60

DEVICE=/dev/$(lsblk -n | awk '$NF != "/" {print $1}')
FS_TYPE=$(file -s $DEVICE | awk '{print $3}')
MOUNT_POINT=/data
echo -e "$DEVICE     $MOUNT_POINT    xfs      defaults,nofail   0   2" >> /etc/fstab

# If no FS, then this output contains "data"
if [ "$FS_TYPE" = "data" ]
then
    echo "Creating file system on $DEVICE"
    mkfs -t xfs $DEVICE
fi

echo -e "$DEVICE     $MOUNT_POINT    xfs      defaults,nofail   0   2" >> /etc/fstab
mount  $MOUNT_POINT

