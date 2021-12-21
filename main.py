def test_bucketing_by_number_of_cycles(count):
    lowCount =0
    mediumCount = 0
    highCount =0 
    print("Counting batteries by usage cycles...\n");
    if count <150:
        lowCount +=1
    elif ((count >150) and (count<649)):
        mediumCount +=1
    else:
        highCount +=1
    print("Done counting :)")
    print (
         lowCount,
         mediumCount,
         highCount
        )


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles(300)
