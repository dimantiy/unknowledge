# Information about OS
uname -a

# Read value to variable
echo -n "Enter Value: "
read my_variable
# OR
read -p "Enter user: " user
read -s "Enter pass: " password

# SSH
ssh-keygen
ssh-agent
ssh-add

# Loop FOR
for VARIABLE in 1 2 3 4 5 .. N
do
	command1
	command2
	commandN
done

# Loop WHILE
while read -r line; do
    echo "... $line ..."
done <<< "$list"

# Replace - sed
# -i '' - inplace replace
# -r    - use regexp Linux
# -E    - use regexp Mac
# &     - placeholder for match
sed -i '' -r "s/[0-9]+/& &/g" path/to/file.txt

# Comporess file/folder
tar -cvf output.tar input/
tar -cvfz output.tgz input/

# Decompress archive
tar -evf input.tar
