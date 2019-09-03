---
layout: post
title: Sublime Merge config
comments: false
---

Windows: Add C:\Program Files\Sublime Merge to your %PATH%

After configuring smerge using the instructions above, run the following from the repository directory:
```bash
git config mergetool.smerge.cmd 'smerge mergetool "$BASE" "$LOCAL" "$REMOTE" -o "$MERGED"'
git config mergetool.smerge.trustExitCode true
git config merge.tool smerge
```

Best regards,

Victor
