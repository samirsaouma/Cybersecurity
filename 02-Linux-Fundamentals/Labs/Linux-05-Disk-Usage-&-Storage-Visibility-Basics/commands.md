# Commands Used

```bash
mkdir linux-storage-lab
cd linux-storage-lab
mkdir reports backups logs
touch reports/report1.txt reports/report2.txt
touch backups/backup1.tar backups/backup2.tar
touch logs/auth.log logs/system.log

echo "Security report baseline" > reports/report1.txt
echo "Disk usage notes" > reports/report2.txt
echo "Failed login from 192.168.1.10" > logs/auth.log
echo "System boot completed" > logs/system.log

yes "log-entry" | head -n 500 > logs/biglog.log
yes "backup-data" | head -n 1000 > backups/bigbackup.txt

ls
ls -R
df -h
du -sh .
du -sh reports backups logs
du -ah . | sort -h | tail -n 10
find . -type f -size +1k