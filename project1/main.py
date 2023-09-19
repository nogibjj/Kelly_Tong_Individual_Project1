import lib
#import pandas

def main():
    """Main function to call data visualization functions"""
    data = lib.load_data("Auto.csv")
                       
    summary = lib.summary_statistics(data)
    print(summary)

    save_visual("scatter_mpg", data)

def save_visual(name, data):
    lib.scatter_mpg(data)
    lib.save_plot(name, data)
    


if __name__ == "__main__":
    main()
