# BankApp

Kullanıcı işlemlerine ve admin yetkilerine dayalı Django bankacılık backend simülasyonu

## Installation

Projenin bir kopyasını edinmek için aşağıdaki komutu çalıştırın.

```bash
git clone github.com/atalar94/bankingApp
```
Django proje klasörüne giderek (manage.py ile aynı dizin) gerekli paket yüklemesini yapın

```bash
pip install -r requirements.txt
```

## Usage

Django proje dizininde veri tabanı migrations işlemlerini aşağıdaki komut ile çalıştırın.

```bash
python manage.py migrate
```
Sunucuyu aşağıdaki komut ile çalıştırarak [127.0.0.1:8000](http://127.0.0.1:8000/) portu üzerinden projenizi deneyin.
```bash
python manage.py runserver
```

## License
[MIT](https://choosealicense.com/licenses/mit/)