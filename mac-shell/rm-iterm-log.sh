#!/bin/bash

# 1ヶ月前の日付を取得
now=$(date +%s)
one_month_ago=$(date -d "1 month ago" +%s)

# ~/log ディレクトリのファイルを取得
files=$(find ~/log -type f)

# 1ヶ月前から編集されていないファイルを削除
for file in $files; do
    last_modified=$(stat -c %y $file)
    if [ $last_modified -le $one_month_ago ]; then
        rm $file
    fi
done