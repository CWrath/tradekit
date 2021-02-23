import db.create_db
import data.populate_stocks
import data.populate_prices


def build_db():
    print(f"Successfully ran" + str(db.create_db))
    print(f"Successfully ran" + str(data.populate_stocks))
    print(f"Successfully ran" + str(data.populate_prices))


if __name__ == '__main__':
    build_db()