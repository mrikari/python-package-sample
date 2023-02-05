# 始める

とりあえず始めるための記録

## pyenvのインストール

```
$ brew install pyenv
$ pyenv install --list
$ export PYTHON_VERSION={インストールしたいバージョン}
$ pyenv install $(PYTHON_VERSION)

# 初回はrehashが必要そう
$ pyenv rehash

$ pyenv global $(PYTHON_VERSION)
```

## poetryのインストール

```
$ curl -sSL https://install.python-poetry.org | python3 -
```

## 仮想環境をつくる

```
$ poetry config virtualenvs.in-project true
$ poetry shell
$ poetry install
```

## モジュールを実行する

```
$ poetry shell
$ python -m mypackage add 1 2
3
```

もしくは

```
$ poetry run python -m mypackage add 1 2
```

## テストを実行する

```
$ poetry run pytest
```

## linter の実行

```
run pysen run lint
```

修正も含める場合

```
run pysen run format
```
　