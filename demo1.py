#Plane Tail numbers
plane_Tail_Numb=['T1','T2','T3','T4','T5','T6']
#Start_Airport at 6:00
start_Airport=['HOUSTONG1','AUSTING1','HOUSTONG2','HOUSTONG3','DALLASG1','DALLASG2']
#Arrival Airport
last_Airport=['AUSTING1','HOUSTONG1','DALLASG1','DALLASG2','HOUSTONG2','HOUSTONG3']
#Journey time from one airport to another
journey_Time={'HOU-AUS':45,'AUS-HOU':45,'HOU-DAL':65,'DAL-HOU':65,'AUS-DAL':50,'DAL-AUS':50}
#Minimum Ground Time
ground_Time={'HOUSTONG1':35,'HOUSTONG2':35,'HOUSTONG3':35,'DALLASG1':30,'DALLASG2':30,'AUSTING1':25}	
#List to store the total flights
Schedule=[]

#To calculate the initial/First departure
dept_Now=[]
for i in range(len(plane_Tail_Numb)):
       dept_Now.insert(i,600)
	   
#Function to convert military time to minutes to midnight
def convertTime_ToMinToMid(time):
    fourDigit=time.zfill(4)
    time=(int(str(fourDigit)[:2])*60)+(int(str(fourDigit)[2:])) 	
    return time
	
#Function to convert minutes to midnight to military time
def convertTime_ToMilitary(time):
    time1=('{:02}'.format(time//60))
    time2=('{:02}'.format(time%60))
    time=str(time1+time2)
    return time

#Function to return Airport name
def airport_Name_Gate (Gate):
    if Gate[:1] == 'A':
        airportName = 'AUS'
        return airportName;
    elif Gate[:1] == 'D':
        airportName = 'DAL'
        return airportName;
    elif Gate[:1] == 'H':
        airportName = 'HOU'
        return airportName;

#Function to change the departure time
def next_Start_Time(start, destination, next_Start):
    next_Start = convertTime_ToMinToMid(next_Start)
    if((start=='HOU' and destination=='AUS')or(start=='AUS' and destination=='HOU')):
        nxtdeparturetime = next_Start - journey_Time[start[:3]+'-'+destination]
        nxtdeparturetime = convertTime_ToMilitary(nxtdeparturetime)
        return nxtdeparturetime;
    elif((start=='DAL' and destination=='AUS')or(start=='AUS' and destination=='DAL')):
        nxtdeparturetime = next_Start - journey_Time[start[:3]+'-'+destination]
        nxtdeparturetime = convertTime_ToMilitary(nxtdeparturetime)
        return nxtdeparturetime;
    elif((start=='DAL' and destination=='HOU')or(start=='HOU' and destination=='DAL')):
        nxtdeparturetime = next_Start - journey_Time[start[:3]+'-'+destination]
        nxtdeparturetime = convertTime_ToMilitary(nxtdeparturetime)
        return nxtdeparturetime;		

#Function to return the journey time
def flight_duration(duration):
    airport_Name=start_Airport[duration][:3]+'-'+last_Airport[duration][:3]
 #   print("Airport Name formed from JourneyTime")
  #  print(airport_Name)
    keysJourney_Time=list(journey_Time)	
    for i in range(len(journey_Time)):
          if(airport_Name==keysJourney_Time[i]):
            return journey_Time.get(airport_Name)
			
Flight_Schedule=[['T1','HOU','AUS','0600','0645'],
                ['T2','AUS','HOU','0600','0645'],
                ['T3','HOU','DAL','0600','0705'],
                ['T4','HOU','DAL','0600','0705'],
                ['T5','DAL','HOU','0600','0705'],
                ['T6','DAL','HOU','0600','0705']]	

#Function to print the data into csv file.			
def PrintSchedule(function, csv_header, flt_sched): 
    with open(function,'wt') as f:
        print(csv_header, file=f) 
        for i in flt_sched:
            print(','.join(i), file=f)	

		
#Function to get the frst arrival time based on departure and destination
arrival=[]
for i in range(len(plane_Tail_Numb)):
   arrival.insert(i,convertTime_ToMilitary(convertTime_ToMinToMid(str(dept_Now[i]))+flight_duration(i)))
AUSG1=arrival[0]
HOUG1=arrival[1]
DALG1=arrival[2]
DALG2=arrival[3]
HOUG2=arrival[4]
HOUG3=arrival[5]

#Function to calculate the next departure time
def next_Departure_Time(arrivalTime,last_Airport): 
    minuArrivalTime=convertTime_ToMinToMid(arrivalTime)
    next_DepartureTime = minuArrivalTime+ground_Time[last_Airport]
    return convertTime_ToMilitary(next_DepartureTime)

#Function to calculate the next arrival time	
def next_Arrival_Time (T, AUSG1, DALG1, DALG2, HOUG1, HOUG2, HOUG3, nxtdpt, Origin):
    nxtdpt = (nxtdpt)
    nxtdpt = convertTime_ToMinToMid(nxtdpt)
    MaxGrndTime=36
    AUSTING1 = convertTime_ToMinToMid(AUSG1)
    DALLASG1 = convertTime_ToMinToMid(DALG1)
    DALLASG2 = convertTime_ToMinToMid(DALG2)
    HOUSTONG1 = convertTime_ToMinToMid(HOUG1)
    HOUSTONG2 = convertTime_ToMinToMid(HOUG2)
    HOUSTONG3 = convertTime_ToMinToMid(HOUG3)
    militarynextarrivalTime=militNextArrival(T,AUSTING1,DALLASG1,DALLASG2,HOUSTONG1 ,HOUSTONG2,HOUSTONG3,nxtdpt,Origin)
    return militarynextarrivalTime

	
#Function to calculate the military next arrival time	
def militNextArrival(T,AUSG1,DALG1,DALG2,HOUG1 ,HOUG2,HOUG3,nxtdepart,start):
 if start[:1] == 'A':
       i = 1
       while (i<36):
            if nxtdepart+50 > DALG1+30:
                    next_arrival_plane = nxtdepart + 50 
                    time_in_milit = convertTime_ToMilitary(next_arrival_plane)
                    military_nextarrivaltime_Dest = time_in_milit + 'DALLASG1'
                    return military_nextarrivaltime_Dest;	
            elif nxtdepart+45 > HOUG3+35:	
                    next_arrival_plane = nxtdepart + 45 
                    time_in_milit = convertTime_ToMilitary(next_arrival_plane)
                    military_nextarrivaltime_Dest = time_in_milit + 'HOUSTONG3'         
                    return military_nextarrivaltime_Dest;					
            elif nxtdepart+45 > HOUG1+35:
                    next_arrival_plane = nxtdepart + 45 
                    time_in_milit = convertTime_ToMilitary(next_arrival_plane)
                    military_nextarrivaltime_Dest = time_in_milit + 'HOUSTONG1'
                    return military_nextarrivaltime_Dest;
            elif nxtdepart+45 > HOUG2+35:
                    next_arrival_plane = nxtdepart + 45 
                    time_in_milit = convertTime_ToMilitary(next_arrival_plane)
                    military_nextarrivaltime_Dest = time_in_milit + 'HOUSTONG2'
                    return military_nextarrivaltime_Dest;					
            elif nxtdepart+50 > DALG2+30:
                    next_arrival_plane = nxtdepart + 50 
                    time_in_milit = convertTime_ToMilitary(next_arrival_plane)
                    military_nextarrivaltime_Dest = time_in_milit + 'DALLASG2'
                    return military_nextarrivaltime_Dest;
            else:
                    nxtdepart = nxtdepart + 1
                    i = i + 1
 elif start[:1] == 'D':
            i = 1
            while (i<36):
                if nxtdepart+50 > AUSG1+25:
                    next_arrival_plane = nxtdepart + 50 
                    time_in_milit = convertTime_ToMilitary(next_arrival_plane)
                    military_nextarrivaltime_Dest = time_in_milit + 'AUSTING1'
                    return military_nextarrivaltime_Dest;  
                elif nxtdepart+65 > HOUG1+35:
                    next_arrival_plane= nxtdepart + 65 
                    time_in_milit = convertTime_ToMilitary(next_arrival_plane)
                    military_nextarrivaltime_Dest = time_in_milit + 'HOUSTONG1'
                    return military_nextarrivaltime_Dest;  
                elif nxtdepart+65 > HOUG2+35:
                    next_arrival_plane = nxtdepart + 65 
                    time_in_milit = convertTime_ToMilitary(next_arrival_plane)
                    military_nextarrivaltime_Dest = time_in_milit+ 'HOUSTONG2'
                    return military_nextarrivaltime_Dest;  
                  
                elif nxtdepart+65 > HOUG3+35:
                    next_arrival_plane = nxtdepart + 65 
                    time_in_milit = convertTime_ToMilitary(next_arrival_plane)
                    military_nextarrivaltime_Dest = time_in_milit + 'HOUSTONG3'
                    return military_nextarrivaltime_Dest;
                else:
                    nxtdepart = nxtdepart + 1
                    i = i + 1
 else:
           i = 1
           while (i<31):
                if nxtdepart+45 > AUSG1+25:
                    next_arrival_plane = nxtdepart + 45 
                    time_in_milit = convertTime_ToMilitary(next_arrival_plane)
                    military_nextarrivaltime_Dest = time_in_milit + 'AUSTING1'
                    return military_nextarrivaltime_Dest;					
                elif nxtdepart+65 > DALG1+30:
                    next_arrival_plane = nxtdepart + 65 
                    time_in_milit = convertTime_ToMilitary(next_arrival_plane)
                    military_nextarrivaltime_Dest = time_in_milit + 'DALLASG1'
                    return military_nextarrivaltime_Dest;  
                elif nxtdepart+65 > DALG2+30:
                    next_arrival_plane = nxtdepart + 65 
                    time_in_milit = convertTime_ToMilitary(next_arrival_plane)
                    military_nextarrivaltime_Dest = time_in_milit + 'DALLASG2'
                    return military_nextarrivaltime_Dest;
                else:
                   nxtdepart = nxtdepart + 1
                   i = i + 1


Origin=[]
Destination=[]
loop=1
while(loop<11): 
    for T in plane_Tail_Numb:
      if T=='T1':
        nextDeptTimeMid=next_Departure_Time(arrival[0],last_Airport[0])
        start_Airport[0]=last_Airport[0]
        military_nextarrivaltime_Dest=next_Arrival_Time(T, arrival[0], arrival[2], arrival[3],arrival[1], arrival[4], arrival[5], nextDeptTimeMid, start_Airport[0])
        military_nextarrivaltime_time = military_nextarrivaltime_Dest[0:4]
        updatedDestination_Name=military_nextarrivaltime_Dest[4:]
        last_Airport[0]=updatedDestination_Name    
        arrival[0]=(military_nextarrivaltime_time)
        if updatedDestination_Name == 'AUSTING1':
                AUSTING1 = int(military_nextarrivaltime_time)
        elif updatedDestination_Name == 'DALLASG1':
                DALLASG1 = int(military_nextarrivaltime_time)
        elif updatedDestination_Name == 'DALLASG2':
                DALLASG2 = int(military_nextarrivaltime_time)
        elif updatedDestination_Name == 'HOUSTONG1':
                HOUSTONG1 = int(military_nextarrivaltime_time)
        elif updatedDestination_Name == 'HOUSTONG2':
                HOUSTONG2 = int(military_nextarrivaltime_time)
        else:
                HOUSTONG3 = int(military_nextarrivaltime_time)
        Origin.insert(0,airport_Name_Gate(start_Airport[0]))
        Destination.insert(0,airport_Name_Gate(last_Airport[0]))
        next_depart= next_Start_Time(Origin[0], Destination[0], military_nextarrivaltime_time)
        SchedT1 = [T, Origin[0], Destination[0], next_depart, military_nextarrivaltime_time]
		
      elif T=='T2':
       nextDeptTimeMid=next_Departure_Time(arrival[1],last_Airport[1])
       start_Airport[1]=last_Airport[1]
       military_nextarrivaltime_Dest=next_Arrival_Time(T, arrival[0], arrival[2], arrival[3],arrival[1], arrival[4], arrival[5], nextDeptTimeMid, start_Airport[1])
       military_nextarrivaltime_time = military_nextarrivaltime_Dest[0:4]
       updatedDestination_Name=military_nextarrivaltime_Dest[4:]
       last_Airport[1]=updatedDestination_Name
       arrival[1]=(military_nextarrivaltime_time)
       if updatedDestination_Name == 'AUSTING1':
             AUSTING1 = int(military_nextarrivaltime_time)
       elif updatedDestination_Name == 'DALLASG1':
             DALLASG1 = int(military_nextarrivaltime_time)
       elif updatedDestination_Name == 'DALLASG2':
             DALLASG2 = int(military_nextarrivaltime_time)
       elif updatedDestination_Name == 'HOUSTONG1':
             HOUSTONG1 = int(military_nextarrivaltime_time)
       elif updatedDestination_Name == 'HOUSTONG2':
             HOUSTONG2 = int(military_nextarrivaltime_time)
       else:
             HOUSTONG3 = int(military_nextarrivaltime_time)
       Origin.insert(1,airport_Name_Gate(start_Airport[1]))
       Destination.insert(1,airport_Name_Gate(last_Airport[1]))
       next_depart= next_Start_Time(Origin[1], Destination[1], military_nextarrivaltime_time)
       SchedT2 = [T, Origin[1], Destination[1], next_depart, military_nextarrivaltime_time]	
	   
      elif T=='T3':
       nextDeptTimeMid=next_Departure_Time(arrival[2],last_Airport[2])
       start_Airport[2]=last_Airport[2]
       military_nextarrivaltime_Dest=next_Arrival_Time(T, arrival[0], arrival[2], arrival[3],arrival[1], arrival[4], arrival[5], nextDeptTimeMid, start_Airport[2])
       military_nextarrivaltime_time = military_nextarrivaltime_Dest[0:4]
       updatedDestination_Name=military_nextarrivaltime_Dest[4:]
       last_Airport[2]=updatedDestination_Name
       arrival[2]=(military_nextarrivaltime_time)
       if updatedDestination_Name == 'AUSTING1':
             AUSTING1 = (military_nextarrivaltime_time)
       elif updatedDestination_Name == 'DALLASG1':
             DALLASG1 = int(military_nextarrivaltime_time)
       elif updatedDestination_Name == 'DALLASG2':
             DALLASG2 = int(military_nextarrivaltime_time)
       elif updatedDestination_Name == 'HOUSTONG1':
             HOUSTONG1 = int(military_nextarrivaltime_time)
       elif updatedDestination_Name == 'HOUSTONG2':
             HOUSTONG2 = int(military_nextarrivaltime_time)
       else:
             HOUSTONG3 = int(military_nextarrivaltime_time)
       Origin.insert(2,airport_Name_Gate(start_Airport[2]))
       Destination.insert(2,airport_Name_Gate(last_Airport[2]))
       next_depart= next_Start_Time(Origin[2], Destination[2], military_nextarrivaltime_time)
       SchedT3 = [T, Origin[2], Destination[2], next_depart, military_nextarrivaltime_time]	
	  
      elif T=='T4':
       nextDeptTimeMid=next_Departure_Time(arrival[3],last_Airport[3])
       start_Airport[3]=last_Airport[3]
       military_nextarrivaltime_Dest=next_Arrival_Time(T, arrival[0], arrival[2], arrival[3],arrival[1], arrival[4], arrival[5], nextDeptTimeMid, start_Airport[3])
       military_nextarrivaltime_time = military_nextarrivaltime_Dest[0:4]
       updatedDestination_Name=military_nextarrivaltime_Dest[4:]
       last_Airport[3]=updatedDestination_Name
       arrival[3]=(military_nextarrivaltime_time)
       
       if updatedDestination_Name == 'AUSTING1':
             AUSTING1 = (military_nextarrivaltime_time)
       elif updatedDestination_Name == 'DALLASG1':
             DALLASG1 = int(military_nextarrivaltime_time)
       elif updatedDestination_Name == 'DALLASG2':
             DALLASG2 = int(military_nextarrivaltime_time)
       elif updatedDestination_Name == 'HOUSTONG1':
             HOUSTONG1 = int(military_nextarrivaltime_time)
       elif updatedDestination_Name == 'HOUSTONG2':
             HOUSTONG2 = int(military_nextarrivaltime_time)
       else:
             HOUSTONG3 = int(military_nextarrivaltime_time)
       Origin.insert(3,airport_Name_Gate(start_Airport[3]))
       Destination.insert(3,airport_Name_Gate(last_Airport[3]))
       next_depart= next_Start_Time(Origin[3], Destination[3], military_nextarrivaltime_time)
       SchedT4 = [T, Origin[3], Destination[3], next_depart, military_nextarrivaltime_time]	 
	 
      elif T=='T5':
       nextDeptTimeMid=next_Departure_Time(arrival[4],last_Airport[4])
       start_Airport[4]=last_Airport[4]
       military_nextarrivaltime_Dest=next_Arrival_Time(T, arrival[0], arrival[2], arrival[3],arrival[1], arrival[4], arrival[5], nextDeptTimeMid, start_Airport[4])
       military_nextarrivaltime_time = military_nextarrivaltime_Dest[0:4]
       updatedDestination_Name=military_nextarrivaltime_Dest[4:]
       last_Airport[4]=updatedDestination_Name
       arrival[4]=(military_nextarrivaltime_time)
       if updatedDestination_Name == 'AUSTING1':
             AUSG1 = (military_nextarrivaltime_time)
       elif updatedDestination_Name == 'DALLASG1':
             DALG1 = int(military_nextarrivaltime_time)
       elif updatedDestination_Name == 'DALLASG2':
             DALG2 = int(military_nextarrivaltime_time)
       elif updatedDestination_Name == 'HOUSTONG1':
             HOUG1 = int(military_nextarrivaltime_time)
       elif updatedDestination_Name == 'HOUSTONG2':
             HOUG2 = int(military_nextarrivaltime_time)
       else:
             HOUG3 = int(military_nextarrivaltime_time)
       Origin.insert(4,airport_Name_Gate(start_Airport[4]))
       Destination.insert(4,airport_Name_Gate(last_Airport[4]))
       next_depart= next_Start_Time(Origin[4], Destination[4], military_nextarrivaltime_time)
       SchedT5 = [T, Origin[4], Destination[4], next_depart, military_nextarrivaltime_time]	 
	        
      else:
       nextDeptTimeMid=next_Departure_Time(arrival[5],last_Airport[5])
       start_Airport[5]=last_Airport[5]
       military_nextarrivaltime_Dest=next_Arrival_Time(T, arrival[0], arrival[2], arrival[3],arrival[1], arrival[4], arrival[5], nextDeptTimeMid, start_Airport[5])
       military_nextarrivaltime_time = military_nextarrivaltime_Dest[0:4]
       updatedDestination_Name=military_nextarrivaltime_Dest[4:]
       last_Airport[5]=updatedDestination_Name
       arrival[5]=(military_nextarrivaltime_time)
       if updatedDestination_Name == 'AUSTING1':
             AUSTING1 = (military_nextarrivaltime_time)
       elif updatedDestination_Name == 'DALLASG1':
             DALLASG1 = int(military_nextarrivaltime_time)
       elif updatedDestination_Name == 'DALLASG2':
             DALLASG2 = int(military_nextarrivaltime_time)
       elif updatedDestination_Name == 'HOUSTONG1':
             HOUSTONG1 = int(military_nextarrivaltime_time)
       elif updatedDestination_Name == 'HOUSTONG2':
             HOUSTONG2 = int(military_nextarrivaltime_time)
       else:
             HOUSTONG3 = int(military_nextarrivaltime_time)
       Origin.insert(5,airport_Name_Gate(start_Airport[5]))
       Destination.insert(5,airport_Name_Gate(last_Airport[5]))
       next_depart= next_Start_Time(Origin[5], Destination[5], military_nextarrivaltime_time)
       SchedT6 = [T, Origin[5], Destination[5], next_depart, military_nextarrivaltime_time]
       
    loop = loop + 1
    TotalSchedule = [SchedT1, SchedT2, SchedT3, SchedT4, SchedT5, SchedT6]
    Flight_Schedule=Flight_Schedule+TotalSchedule
    print(Flight_Schedule)	
    header = 'tail_number,origin,destination,departure_time,arrival_time'
    file_name_csv = 'flight_schedule.csv'
    Flight_Schedule = sorted(Flight_Schedule, key = lambda x: x[0] + x[3])
    PrintSchedule(file_name_csv, header, Flight_Schedule)	
	

