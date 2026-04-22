# Commands Used

```bash
mkdir linux-permissions-lab
cd linux-permissions-lab
touch notes.txt script.sh private.txt
ls -l

chmod 644 notes.txt
chmod 700 script.sh
chmod 600 private.txt
ls -l

echo "Security Notes" > notes.txt
echo "echo hello" > script.sh
echo "private content" > private.txt

cat notes.txt
cat private.txt

chmod +x script.sh
./script.sh