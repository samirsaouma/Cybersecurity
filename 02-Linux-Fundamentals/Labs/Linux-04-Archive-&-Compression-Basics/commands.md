# Commands Used

```bash
mkdir linux-archive-lab
cd linux-archive-lab
mkdir notes logs
touch notes/security.txt
touch notes/network.txt
touch logs/auth.log
touch logs/system.log

echo "Security hardening checklist" > notes/security.txt
echo "Network baseline notes" > notes/network.txt
echo "Failed login from 192.168.1.10" > logs/auth.log
echo "System startup complete" > logs/system.log

ls
ls notes
ls logs
cat notes/security.txt
cat logs/auth.log

tar -cvf lab-archive.tar notes logs
tar -czvf lab-archive.tar.gz notes logs

tar -tvf lab-archive.tar
tar -tzvf lab-archive.tar.gz

mkdir extracted
tar -xzvf lab-archive.tar.gz -C extracted

ls extracted
ls extracted/notes
ls extracted/logs