import lib
import pandas

def main():
    """Main function to call data visualization functions"""
    data = pd.read_csv("Auto.csv)
                       
    summary = lib.summary_statistics(data)
    print(summary)

    save_visual("MPG vs Weight", data)

def save_visual(name, data):
    lib.scatter_mpg(data)
    lib.save_plot(name, data)
    


if __name__ == "__main__":
    main()
