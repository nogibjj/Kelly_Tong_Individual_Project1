#This is the python script that describe the statistics
import lib
#import pandas

def main():
    """Main function to call data visualization functions"""
    
    data() 
                       
    summary = lib.describe_dataset(data)
    print(summary)

    lib.scatter_mpg(data)

    lib.fitted_mpg(data)

    lib.scatter_acc(data)

    lib.fitted_acc(data)

    lib.generate_general_markdown(data)

def data():
    data = "project1/Auto.csv"
    return data

if __name__ == "__main__":
    main()
