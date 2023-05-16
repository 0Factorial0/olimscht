# Man In The Middle Protection V1

Fake Requests Without Downloading The Surfed Pages.

Some Websites May Not Work Due To The Log-In Systems They Use.

<p align="center" width="100%">
    <img width="99%" src="https://gitlab.com/0Factorial0/python-mitm-protection/-/raw/master/content/screenshot/crawl.png">
</p>

<p align="center" width="100%">
    <img width="99%" src="https://gitlab.com/0Factorial0/python-mitm-protection/-/raw/master/content/screenshot/request.png">
</p>

## Installing

1. Install The Git Client: https://git-scm.com/downloads
2. Get Python3: https://www.python.org/downloads/
    - Or Use Homebrew: https://docs.brew.sh/Installation
    - Install Latest Python With The Terminal Command: `brew install python` 
3. CMD, Git Bash, Terminator, iTerm, Guake, Zsh Or And Terminal Works.
4. Connect Your Git Account:
    -  `git config --global user.name "<username>"`
    -  `git config --global user.email "<e-mail>"`
5. Clone The Project To Your System: `git clone https://gitlab.com/0Factorial0/python-mitm-protection.git`
6. Go Inside Of The Folder: `cd <file_name>`, `cd ..`
7. Start The Program With: `python3 start.py`
8. Or Use `python3 start.py --gui java` To Start With Java GUI.

## Usage

For Help
1. `python3 start.py --h`
2. `python3 start.py --help`

Use From Terminal Or Java GUI. (Best Is To Open Two Terminals, One For Crawler, One For Requester)

Extracts (Unique)Links From URL File(First 200 Per URL[change here: spider/crawler.py[73:23]]): `spider/url/sites.txt` And Puts Them In The `spider/link/links.txt` Using Hardcoded `python3 spider/crawler.py --file spider/url/sites.txt --output spider/link/links.txt` Terminal Command.

Then Using This Command For Sending The List To Requester: `python3 content/requester.py --list spider/link/links.txt`

Requester Cuts A Part Of Your List And Browses That. And Calls Back Itself When It Finishes With A Different Array.

<p align="center" width="100%">
    <img width="99%" src="https://gitlab.com/0Factorial0/python-mitm-protection/-/raw/master/content/screenshot/array.png">
</p>

Requester Is Sending A Request Every 1 Second. If You Want To Change That, Go To content/requester.py[8:16]

Opening Interface:
1. `python3 start.py --gui java`

Java Works For 360 Seconds At A Time. To Change Go To: content/execute.java[115:45] and content/generate.java[109:45]

Opening Two Terminals:
1. First Terminal To `python3 start.py --go crawl`
2. Second Terminal To `python3 start.py --go request`

Opening Them One After Another(xTerm) Or At The Same Time(CMD):
1. `python3 start.py --go crazy`

## Notes

If You Want To Close The Crawler Or Requester You Will Need To Open Another Terminal And Start The Program In Terminal Using `python3 start.py` And Select The "Kill Python" On The Menu.

Or This Shortcut:
1. `python3 start.py --k p`

content/test.java Is To Use Speedtest CLI. You Can Download Here:
https://www.speedtest.net/apps/cli

Put Your Folder To content/speedtest/ And Make The Folder Name One Of These: (win, linux, mac)

content/test2.java Is To Use Tshark. You Can Download Here:
https://tshark.dev/

#0x0 #11unx0 #aovaa