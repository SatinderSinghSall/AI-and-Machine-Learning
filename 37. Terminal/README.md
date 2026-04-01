# 🖥️ Terminal (Command Line) – Complete Guide

A **Terminal** is a text-based interface that allows you to interact with your computer using commands instead of a graphical interface (GUI).

You can:

- Navigate folders
- Create/delete files
- Run programs
- Install packages
- Automate tasks
- Manage Git & servers

Works on:

- macOS → Terminal
- Linux → Shell/Bash
- Windows → PowerShell / Git Bash / WSL

---

# 📍 Table of Contents

1. Basic Concepts
2. Navigation Commands
3. File & Directory Commands
4. File Viewing Commands
5. Editing & Managing
6. Search & Filters
7. Permissions
8. Processes
9. Networking
10. Advanced Shell Features
11. Shortcuts & Productivity
12. Pro Tips

---

# 1️⃣ Basic Concepts

## Important Terms

| Term      | Meaning                                   |
| --------- | ----------------------------------------- |
| Terminal  | App to type commands                      |
| Shell     | Program that executes commands (bash/zsh) |
| Command   | Instruction you type                      |
| Path      | Location of a file/folder                 |
| Directory | Folder                                    |

---

# 2️⃣ Navigation Commands (Beginner)

## pwd

Print current directory

```bash
pwd
```

````

Example:

```
/home/user/Documents
```

---

## ls

List files

```bash
ls
ls -l
ls -a
ls -la
```

Options:

- `-l` → details
- `-a` → hidden files
- `-h` → readable sizes

---

## cd

Change directory

```bash
cd foldername
cd ..
cd ~
cd /
```

Examples:

```bash
cd Documents
cd ..
cd ~/Downloads
```

---

# 3️⃣ File & Directory Commands

## mkdir

Create folder

```bash
mkdir project
mkdir -p src/components
```

---

## touch

Create empty file

```bash
touch index.js
```

---

## cp

Copy files

```bash
cp file.txt backup.txt
cp -r folder copyFolder
```

---

## mv

Move or rename

```bash
mv file.txt new.txt
mv file.txt folder/
```

---

## rm

Delete

```bash
rm file.txt
rm -r folder
rm -rf folder   # force delete
```

⚠️ Be careful with `-rf`

---

# 4️⃣ File Viewing Commands

## cat

Show full file

```bash
cat file.txt
```

---

## less

Scrollable view

```bash
less file.txt
```

Press:

- q → quit

---

## head

```bash
head file.txt
head -n 5 file.txt
```

---

## tail

```bash
tail file.txt
tail -f logs.txt
```

Useful for logs

---

# 5️⃣ Editing & Managing

## nano (simple editor)

```bash
nano file.txt
```

Save → Ctrl + O
Exit → Ctrl + X

---

## echo

```bash
echo "Hello"
echo "Hello" > file.txt
echo "Add line" >> file.txt
```

---

## clear

```bash
clear
```

---

# 6️⃣ Search & Filters

## grep

```bash
grep "error" file.txt
grep -r "hello" .
```

---

## find

```bash
find . -name "*.js"
find . -type d
```

---

## wc

```bash
wc file.txt
wc -l file.txt
```

Counts lines/words

---

## sort

```bash
sort file.txt
```

---

## uniq

```bash
uniq file.txt
```

---

# 7️⃣ Permissions

## chmod

```bash
chmod 777 file.sh
chmod +x script.sh
```

Permission types:

- r → read
- w → write
- x → execute

---

## chown

```bash
sudo chown user file.txt
```

---

# 8️⃣ Processes

## ps

```bash
ps
ps aux
```

---

## top

```bash
top
```

Live processes

---

## kill

```bash
kill 1234
kill -9 1234
```

---

# 9️⃣ Networking

## ping

```bash
ping google.com
```

---

## curl

```bash
curl https://example.com
```

---

## wget

```bash
wget file_url
```

---

# 🔟 Advanced Shell Features

## Pipes |

```bash
cat file.txt | grep hello
```

---

## Redirection

```bash
>   overwrite
>>  append
<   input
```

Example:

```bash
ls > list.txt
```

---

## &&

Run next only if first succeeds

```bash
mkdir test && cd test
```

---

## ||

Run if first fails

```bash
mkdir test || echo "Failed"
```

---

## Variables

```bash
name="John"
echo $name
```

---

## Aliases

```bash
alias ll="ls -la"
```

---

## History

```bash
history
!10
```

---

# 1️⃣1️⃣ Shortcuts

| Shortcut | Action           |
| -------- | ---------------- |
| Tab      | Auto-complete    |
| ↑        | Previous command |
| Ctrl + C | Stop             |
| Ctrl + L | Clear            |
| Ctrl + A | Start of line    |
| Ctrl + E | End of line      |
| Ctrl + R | Search history   |

---

# 1️⃣2️⃣ Pro Tips

✅ Use Tab completion
✅ Use aliases
✅ Avoid rm -rf unless sure
✅ Use less for large files
✅ Combine commands with pipes

---

# 🚀 Practice Tasks

Try:

```bash
mkdir demo
cd demo
touch a.txt b.txt
echo "hello" > a.txt
cp a.txt copy.txt
ls -la
grep hello a.txt
```

---

# 🎯 Conclusion

Mastering the terminal:

- saves time
- improves productivity
- is essential for developers
- required for Git, Docker, Servers, AI/ML

Practice daily 🚀
````
