# Machine Learning Template (ml_template)

**Note: Japanese description available in the latter part of this document.**

**注意：このドキュメントの後半部分に日本語の説明が含まれています。**

## English Description

The `ml_template` repository is a streamlined template configured for machine learning projects, particularly tailored for Kaggle competitions.

Instructions:

- Clone the repository.
- Adapt the template according to the project requirements.

Directory Structure:

```
/ml_template
|-- /src
|  |-- /models # Store core scripts for modeling
|  |-- /data # Scripts for data processing (data loading, preprocessing, etc.)
|  `-- /utils # Store auxiliary functions and classes (split the directory as needed since it's an anti-pattern to keep everything here)
|
|-- /notebooks # Used for EDA, data analysis, and model prototyping
|
|-- /scripts # Store shell scripts (e.g.,train.sh)
|
|-- /data
|  |-- /raw # Store raw data (For Kaggle code competitions, download to `/kaggle/input/`)
|  `-- /processed # Store processed data
|
|-- /docs # Documentation of the project, usage, examples, etc.
|
|-- /tests # Test scripts (rarely used in Kaggle)
|
|-- README.md # Project overview, installation method, examples, etc.
|
|-- requirements.txt # List of dependencies and libraries
|
`-- .gitignore # Specify files and directories to be excluded from git tracking
```

## Environment Setup

We assume the use of the official Kaggle Docker image (similar to the Kaggle environment, data storage is in `/kaggle/input/`).

For detailed instructions and additional information on using the Kaggle Docker image, please refer to [kaggle docker custom (coming soon)](https://github.com/yiiino/).

## 日本語の説明

この`ml_template`リポジトリは、短期間の機械学習プロジェクト（Kaggleコンペティションなど）向けに構成された簡易テンプレートです。

使用方法：

- リポジトリをクローンする。
- プロジェクトの要件に応じてテンプレートを適応する。

ディレクトリ構成:

```
/ml_template
|-- /src
|   |-- /models      # モデリングにおいてコアとなるスクリプトを格納
|   |-- /data        # データ処理用スクリプト（データの読み込み、前処理など）
|   `-- /utils       # 補助的な関数やクラスを格納（`utils`という命名はアンチパターンなので適宜細かくディレクトリを切り分ける）
|
|-- /notebooks       # EDAやデータ分析、モデルのプロトタイピングに使用
|
|-- /scripts         # シェルスクリプト（`train.sh`など）を格納する
|
|-- /data
|   |-- /raw         # 生データを格納（Kaggleのコードコンペティションの場合は、`/kaggle/input/`にダウンロード）
|   `-- /processed   # 前処理済みデータ
|
|-- /docs            # プロジェクトのドキュメンテーション、使用方法、例など
|
|-- /tests           # テストスクリプト（Kaggleではほぼ使わない）
|
|-- README.md        # プロジェクトの概要、インストール方法、使用例など
|
|-- requirements.txt # 必要な依存関係やライブラリをリストアップ
|
`-- .gitignore       # gitの追跡から除外するファイルやディレクトリを指定
```

## 環境構築

Kaggle 公式の Docker イメージを使用することを前提とします（Kaggle 環境と同じく、データ格納は`/kaggle/input/`）。

Kaggle Docker イメージの使用方法と詳細な指示については、[kaggle docker custom (近日公開)](https://github.com/yiiino/)を参照ください。
