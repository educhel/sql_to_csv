import argparse
import pandas as pd
from sqlalchemy import create_engine

# --- 설정 (Configuration) ---
PASSWORD = "testtest"
DATABASE_URL = f"mysql+pymysql://root:{PASSWORD}@127.0.0.1:3306/sakila"


def export_db_to_csv(query: str, output_path: str, db_url: str):
    """
    데이터베이스에 쿼리를 실행하여 결과를 CSV 파일로 저장하는 함수
    """
    engine = None
    try:
        engine = create_engine(db_url)
        print("✅ 데이터베이스 연결 성공")

        print(f"쿼리 실행:\n{query}") # 쿼리 내용을 확인하기 위해 출력
        df = pd.read_sql(query, engine)
        print("✅ 데이터 로드 성공")

        df.to_csv(output_path, index=False, encoding='utf-8-sig')
        print(f"✅ '{output_path}' 파일로 저장 완료")

    except Exception as e:
        print(f"❌ 처리 중 오류 발생: {e}")

    finally:
        if engine:
            engine.dispose()
            print("🔗 데이터베이스 연결 종료")


def main():
    """
    프로그램의 메인 로직을 실행하는 함수
    """
    parser = argparse.ArgumentParser(description="MySQL 쿼리 파일의 결과를 CSV 파일로 내보냅니다.")
    parser.add_argument("query_file", type=str, help="실행할 .sql 파일의 경로")
    parser.add_argument("output_path", type=str, help="저장할 CSV 파일의 경로")
    args = parser.parse_args()

    try:
        # .sql 파일을 읽어서 쿼리 문자열로 가져옵니다.
        with open(args.query_file, 'r', encoding='utf-8') as f:
            sql_query = f.read()
    except FileNotFoundError:
        print(f"❌ 오류: '{args.query_file}' 파일을 찾을 수 없습니다.")
        return # 파일이 없으면 프로그램 종료

    print("--- 데이터 내보내기 시작 ---")
    export_db_to_csv(query=sql_query, output_path=args.output_path, db_url=DATABASE_URL)
    print("--- 모든 작업 완료 ---")


if __name__ == "__main__":
    main()