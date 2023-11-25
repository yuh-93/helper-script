# reorganize_release_notes
## 概要
GitHubのリリースノートで自動生成されたノートを再編成し整理するPythonスクリプトです。
リリースノート内の各変更点を特定のカテゴリ（例えば「feat」、「fix」、「docs」）ごとにグループ化します。
## ファイル説明
- input.md
    - githubのリリース時に自動生成された文章を記載してください 
- output.md
    - 再編成されたファイル
## 実行方法
```bash
python reorganize_release_notes.py
```
## テスト方法
reorganize_release_noteディレクトリにて実行
```bash
python3 -m unittest tests.test_main
```