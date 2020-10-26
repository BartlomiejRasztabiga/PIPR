# Zadanie 1
``` bash
git clone --depth 1 https://github.com/torvalds/linux
grep --include=\*.{c,h} -rnw 'linux/' -e "dragons" > dragons
```

# Zadanie 2
``` bash
(date +"%H:%M %A, %d/%m/%Y"; cat /etc/os-release) > my-release
```

# Zadanie 3
``` bash
scp brasztab@lab09011.elka.pw.edu.pl:~lneumann/pipr/lab2_logs.csv lab2_logs.csv
cat lab2_logs.csv | grep 'https\?://ox.ac.uk' | sort | cut -f 1 -d , | uniq -c > adresy
```