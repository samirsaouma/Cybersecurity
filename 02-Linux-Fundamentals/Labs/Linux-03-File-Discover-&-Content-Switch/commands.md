# Commands Used

```bash
mkdir linux-search-lab
cd linux-search-lab
mkdir logs notes configs
touch notes/security.txt
touch notes/network.txt
touch configs/app.conf
touch logs/auth.log
touch logs/system.log

echo "Security baseline notes" > notes/security.txt
echo "Network troubleshooting notes" > notes/network.txt
echo "auth_enabled=true" > configs/app.conf
echo "Failed login from 192.168.1.10" > logs/auth.log
echo "System boot completed" > logs/system.log

ls
cd linux-search-lab
ls
cd configs
ls
cat app.conf

find -name "*.txt"
find -name "*.log"

grep -r "login"
grep -r "auth_enabled"
grep -r "notes"