#This is the python script that describe the statistics
import lib
#import pandas

def main():
    """Main function to call data visualization functions"""
    data = "Auto.csv"
                       
    summary = lib.describe_dataset(data)
    print(summary)

    #lib.scatter_mpg(data)

    #save_visual("scatter_mpg", data)

    #test_fitted_mpg(data)

    #lib.generate_general_markdown(data)

#def save_visual(name, data):
    #lib.scatter_mpg(data)
    #lib.save_plot(name, data)

#def test_fitted_mpg(data):
    #lib.fitted_mpg(data)


if __name__ == "__main__":
    main()
