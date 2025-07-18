# SQL to CSV
> sql에서 csv를 뽑는 방법입니다.

## 기본 조건
```
# 가상환경 세팅
python -m venv .venv

# 본인 환경에 맞춰 가상환경 활성화
# win
. .venv/Script/activate

# mac
source .venv/bin/activate

# 설치
python -m pip install argparse pandas sqlalchemy cryptography pymysql
```

## 실행 방법
터미널에서 첫 번째 인자로 `.sql` 파일의 경로를 넘겨주면 됩니다.

명령어 형식:
```
python <스크립트_이름> <SQL_파일_경로> <저장할_파일_경로>
```

실행 예시:
```bash
python main.py my_query.sql action_films.csv
```

이렇게 하면 main.py 스크립트가 my_query.sql 파일을 읽어 그 안의 쿼리를 실행하고, 결과를 action_films.csv 파일로 저장해 줍니다.







