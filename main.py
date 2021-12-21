def test_bucketing_by_number_of_cycles(count):
    lowCount =0
    mediumCount = 0
    highCount =0
    for i in count: 
        print("Counting batteries by usage cycles...\n");
        if count[i] <150:
            lowCount +=1
        elif ((count[i] >150) and (count[i]<649)):
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
  test_bucketing_by_number_of_cycles([300,500,600])
