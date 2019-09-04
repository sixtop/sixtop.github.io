---
layout: post
title: Bash prompt here in Windows Explorer Context Menu
comments: false
---

Install chere and execute as admin:
```
chere -i -t mintty -s bash
```

Change the following registry:
```
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\background\shell\cygwin_bash
```
and edit so it says ```&Open Cygwin Prompt Here```
