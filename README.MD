### django_web_authの基本機能
- ユーザー認証 (User Authentication)
- Webアプリ： todo_task(画面:Bootstrap, タスクのCRUD機能)
- 開発環境： Django, Database(SQlite, または、PostgreSQL、MySQL)
-          Docker-compose(Databaseのみ、または、全環境（Web+App+DB)

### django_web_auth
| カテゴリ             | 機能                                                                 |
|----------------------|---------------------------------------------------------------------|
| ユーザー登録と認証   | - ユーザー登録 (Sign Up) <br> - ユーザーログイン (Login) <br> - ユーザーログアウト (Logout) |
| パスワード管理       | - パスワードリセット (Password Reset) <br> - パスワード変更 (Password Change) <br> - パスワードセット (Password Set) |
| ソーシャルアカウント認証 | - ソーシャルログイン (Social Login) <br> - ソーシャルアカウントのリンクとアンリンク |
| アカウント管理       | - メールアドレス管理 (Email Management) <br> - ユーザープロファイル (User Profile) |
| セッション管理       | - セッション管理 (Session Management) |
| 多要素認証 (MFA)     | - 多要素認証 (Multi-Factor Authentication) |
| レート制限           | - レート制限 (Rate Limiting) |
| 管理ツール           | - Django Adminとの統合 |
| 国際化 (i18n)        | - 多言語対応 |
| 拡張とカスタマイズ   | - カスタムビューとフォーム <br> - シグナル |
#### ER図

![ER.png](assets/ER.png)
