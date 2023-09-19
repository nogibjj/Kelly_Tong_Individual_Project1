import lib
import pandas

def main():
    """Main function to call data visualization functions"""
    data = pd.read_csv("Auto.csv)
                       
    summary = lib.summary_statistics(data)
    print(summary)


if __name__ == "__main__":
    main()
