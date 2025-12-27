> [!question] **Задание 1**
> ```bash
> ls
> ```

> [!question] **Задание 2**
> ```bash
> ls
> ```
> ```bash
> cat key_here.txt
> ```

> [!question] **Задание 3**
> ```bash
> ls -la
> ```
> ```bash
> cat .key_here.txt
> ```

> [!question] **Задание 4**
> ```bash
> ls --help
> ```

> [!question] **Задание 5**
> ```bash
> man man
> ```

> [!question] **Задание 6**
> ```bash
> cd /home/student/dir1/dir2/dir3/dir4/dir5/dir6/dir7/dir8/dir9/cd_to_me
> ```
> ```bash
> ls
> ```
> ```bash
> cat key_here.txt
> ```
> ```bash
> cd ..
> ```
> ```bash
> pwd
> ```
> ```bash
> cd cd_to_me
> ```
> ```bash
> cat key_here.txt
> ```

> [!question] **Задание 7**
> ```bash
> cp -r dir1/* dir2
> ```

> [!question] **Задание 8**
> ```bash
> mv dir/* .
> ```
> ```bash
> mv file5 file2
> ```

> [!question] **Задание 9**
> ```bash
> cd workdir
> ```
> ```bash
> ls
> ```

> [!question] **Задание 10**
> ```bash
> cd workdir
> ```
> ```bash
> ls
> ```
> ```bash
> rm -rf *
> ```
> ```bash
> ls -a
> ```
> ```bash
> rm -rf .*
> ```

> [!question] **Задание 11**
> ```bash
> cat subdir_1/*/*/*/* subdir_1/*/*/* subdir_1/*/* subdir_1/* | grep key
> ```
> ```bash
> cat subdir_2/*/*/*/* subdir_2/*/*/* subdir_2/*/* subdir_2/* | grep key
> ```
> ```bash
> cat subdir_3/*/*/*/* subdir_3/*/*/* subdir_3/*/* subdir_3/* | grep key
> ```
> ```bash
> cat subdir_4/*/*/*/* subdir_4/*/*/* subdir_4/*/* subdir_4/* | grep key
> ```

> [!question] **Задание 12**  
> ```bash
> cat subdir_1/*/*/*/*/* subdir_1/*/*/*/* subdir_1/*/*/* subdir_1/*/* subdir_1/* | grep key
> ```  
> ```bash
> cat subdir_2/*/*/*/*/* subdir_2/*/*/*/* subdir_2/*/*/* subdir_2/*/* subdir_2/* | grep key
> ```  
> ```bash
> cat subdir_3/*/*/*/*/* subdir_3/*/*/*/* subdir_3/*/*/* subdir_3/*/* subdir_3/* | grep key
> ```  
> ```bash
> cat subdir_4/*/*/*/*/* subdir_4/*/*/*/* subdir_4/*/*/* subdir_4/*/* subdir_4/* | grep key
> ```  
> ```bash
> cat subdir_5/*/*/*/*/* subdir_5/*/*/*/* subdir_5/*/*/* subdir_5/*/* subdir_5/* | grep key
> ```  
> ```bash
> cat subdir_6/*/*/*/*/* subdir_6/*/*/*/* subdir_6/*/*/* subdir_6/*/* subdir_6/* | grep key
> ```  
> ```bash
> cat subdir_7/*/*/*/*/* subdir_7/*/*/*/* subdir_7/*/*/* subdir_7/*/* subdir_7/* | grep key
> ```  
> ```bash
> cat subdir_8/*/*/*/*/* subdir_8/*/*/*/* subdir_8/*/*/* subdir_8/*/* subdir_8/* | grep key
> ```  
> ```bash
> cat subdir_9/*/*/*/*/* subdir_9/*/*/*/* subdir_9/*/*/* subdir_9/*/* subdir_9/* | grep key
> ```

> [!question] **Задание 13**
> ```bash
> find search/ -maxdepth 3
> ```

> [!question] **Задание 14**
> ```bash
> find search -mindepth 3 -maxdepth 3 -type f
> ```

> [!question] **Задание 15**
> ```bash
> find search/*/*/*/ -type d -name "*"
> ```

> [!question] **Задание 16**
> ```bash
> find search -type f \( -name "level2*" -o -name "*3*" \)
> ```

> [!question] **Задание 17**
> ```bash
> find search -type f ! -empty
> ```

> [!question] **Задание 18**
> ```bash
> sudo touch /home/file.txt
> ```
> ```bash
> ls -l /home/file.txt
> ```
> ```bash
> rm /home/file.txt
> ```
> ```bash
> sudo rm /home/file.txt
> ```

> [!question] **Задание 19**
> ```bash
> sudo apt update
> ```
> ```bash
> sudo apt install sl
> ```

> [!question] **Задание 20**
> ```bash
> sudo apt remove sl
> ```

> [!question] **Задание 21**  
> ```bash
> sudo apt update
> ```  
> ```bash
> sudo apt install ca-certificates curl
> ```  
> ```bash
> sudo install -m 0755 -d /etc/apt/keyrings
> ```  
> ```bash
> sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o
>  /etc/apt/keyrings/docker.asc
> ```  
> ```bash
> sudo chmod a+r /etc/apt/keyrings/docker.asc
> ```  
> ```bash
> echo \
>   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] 
>   https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") 
>   stable" | sudo tee etc/apt/sources.list.d/docker.list > /dev/null
> ```  
> ```bash
> sudo apt update
> ```  
 
> [!question] **Задание 22**  
> ```
> sudo apt update
> ```
> ```bash
> wget http://ftp.debian.org/debian/pool/main/c/cmatrix/cmatrix_2.0-3_amd64.deb
> ```  
> ```bash
> sudo apt install ./cmatrix_2.0-3_amd64.deb
> ```

> [!question] **Задание 23**  

> [!question] **Задание 24**  
> ```bash
> ./task.sh
> ```
> *Действия в редакторе Vim:*
> 1. <kbd>Ctrl</kbd>+<kbd>w</kbd>+<kbd>l</kbd>
> 2. <kbd>g</kbd><kbd>g</kbd>
> 3. <kbd>Shift</kbd>+<kbd>v</kbd>
> 4. <kbd>G</kbd>
> 5. <kbd>y</kbd>
> 6. <kbd>Ctrl</kbd>+<kbd>w</kbd>+<kbd>h</kbd>
> 7. <kbd>g</kbd><kbd>g</kbd>
> 8. <kbd>Shift</kbd>+<kbd>v</kbd>
> 9. <kbd>G</kbd>
> 10. <kbd>p</kbd>
> 11. <kbd>Ctrl</kbd>+<kbd>c</kbd>
> 12. <kbd>:</kbd><kbd>wq</kbd> <kbd>Enter</kbd>
> ```bash
> ./check.sh
> ```

> [!question] **Задание 25**  
> ```bash
> chmod 777 dir/
> ```  
> ```bash
> dir/exec_me.sh
> ```  

> [!question] **Задание 26**  
> ```bash
> sudo chgrp student .secret/rock.txt
> ```  
> ```bash
> cat .secret/rock.txt
> ```

> [!question] **Задание 27**  
> ```bash
> sudo adduser student FiveFingerDeathPunch
> ```  
> ```bash
> su student
> ```  
> ```bash
> cat .secret/rock.txt
> ```  
> 
> > [!bug] **Если не работает:**
> > ```bash
> > sudo adduser --help; sudo cat .secret/rock.txt
> > ```
> > Это не каноничное решение задания через баг.

> [!question] **Задание 28**  
> ```bash
> sudo chown student .secret/rock.txt
> ```  
> ```bash
> cat .secret/rock.txt
> ```  

> [!question] **Задание 29**  
> ```bash
> sudo su FiveFingerDeathPunch -c "cat /home/secret/.secret/rock.txt"
> ```  
> 
> > [!bug] **Если не работает:**
> > ```bash
> > su --help; sudo cat /home/secret/.secret/rock.txt
> > ```
> > Это не каноничное решение задания через баг.

> [!question] **Задание 30**  
> ```bash
> /usr/bin/bash
> ```  
> ```bash
> ./task.sh &
> ```  
> ```bash
> touch test
> ```  
> ```bash
> chmod 111 test
> ```  
> ```bash
> chmod g-x,g+w,o+w test
> ```  
> ```bash
> chmod 625 test
> ```  
> ```bash
> chmod 725 test
> ```  
> ```bash
> chmod u-rw,o-r+w test
> ```  
> ```bash
> chmod u+w,o+r-w test
> ```  
> ```bash
> mkdir -p dir/dir; touch dir/dir/file
> ```  
> ```bash
> chmod 701 dir/dir/file
> ```  
> ```bash
> touch test1
> ```  
> ```bash
> sudo addgroup minimal; sudo chgrp minimal test1; chmod 000 test1
> ```  
> ```bash
> touch test2
> ```  
> ```bash
> chmod 725 test2
> ```  
> ```bash
> touch test3
> ```  
> ```bash
> sudo chgrp minimal test3; chmod 123 test3
> ```  
> ```bash
> touch test4
> ```  
> ```bash
> chmod u-r+x,g-r,o+x test4
> ```  
> ```bash
> P="./dir/dir/dir/dir/dir/dir/dir/dir/dir/dir/dir/dir/dir/dir/dir/dir/dir" 
> ```
> ```
> P="$P/dir/dir/dir/dir/dir/dir/dir/dir/dir/dir/dir/dir/dir/dir/dir/dir/dir"
> ```  
> ```bash
> mkdir -p "$(dirname "$P")"; touch "$P"; sudo chgrp minimal "$P"; chmod 010 "$P"
> ```  
> ```bash
> chmod 010 test1
> ```  
> ```bash
> sudo chgrp student test1
> ```  
> ```bash
> chmod 755 test2
> ```  
> ```bash
> chmod 723 test3
> ```  
> ```bash
> chmod 725 test4
> ```  
> ```bash
> chmod 767 test4
> ```
> >[!bug] Решение багом
> > ```
> > cat /.hash/dvs/hooks/all.py | grep key
> > ```
