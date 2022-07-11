from des import SchedulerDES
from event import Event, EventTypes 
from process import Process, ProcessStates 



class FCFS(SchedulerDES):
        
    def scheduler_func(self, cur_event):
        
       
         for p in self.processes:
           
             if p.process_state == ProcessStates.READY:
                return p
        
        
      

    def dispatcher_func(self, cur_process):
        cur_process.run_for(cur_process.remaining_time,self.time)
        cur_process.process_state=ProcessStates.TERMINATED
    
        #cur_process.run_for(cur_process.service_time,cur_process._service_time)
        
        #cur_process.run_for(cur_process.remaining_time,self.time)
        new_event = Event(process_id=cur_process.process_id, event_time= cur_process.departure_time, event_type=EventTypes.PROC_CPU_DONE)
       
        return new_event


class SJF(SchedulerDES):
    def scheduler_func(self, cur_event):
        for num  in range(len(self.processes)-1,0,-1):
            for i in range(num):
                if self.processes[i].service_time>self.processes[i+1].service_time:
                    temp = self.processes[i]
                    self.processes[i] = self.processes[i+1]
                    self.processes[i+1] = temp
        for p in self.processes:
             if p.process_state == ProcessStates.READY:
            
                return p
        

    def dispatcher_func(self, cur_process):
        cur_process.run_for(cur_process.remaining_time,self.time)
        cur_process.process_state=ProcessStates.TERMINATED
    
        #cur_process.run_for(cur_process.service_time,cur_process._service_time)
        
        #cur_process.run_for(cur_process.remaining_time,self.time)
        new_event = Event(process_id=cur_process.process_id, event_time= cur_process.service_time+self.time, event_type=EventTypes.PROC_CPU_DONE)
        
        return new_event 


class RR(SchedulerDES):
    
    
    def scheduler_func(self, cur_event):
        a = cur_event._process_id # gets the process id which will be used to index
        cur_process = self.processes[a]
       
       
        return cur_process
         

    def dispatcher_func(self, cur_process):
        cur_process.run_for(self.quantum,self.time)
        
        if cur_process.remaining_time>0.0:
           
            
            
            new_event = Event(process_id=cur_process.process_id, event_time=self.quantum+self.time , event_type=EventTypes.PROC_CPU_REQ)
            
            
        else:
            cur_process.process_state=ProcessStates.TERMINATED
           
            new_event = Event(process_id=cur_process.process_id, event_time= cur_process.departure_time, event_type=EventTypes.PROC_CPU_DONE)
    
       
        return new_event 


class SRTF(SchedulerDES):
    def scheduler_func(self, cur_event):
        for num  in range(len(self.processes)-1,0,-1):
            for i in range(num):
                if self.processes[i].remaining_time>self.processes[i+1].remaining_time:
                    temp = self.processes[i]
                    self.processes[i] = self.processes[i+1]
                    self.processes[i+1] = temp
                if self.processes[i].remaining_time == self.processes[i+1].remaining_time: ##trying to implement when two have the same service time
                    if self.processes[i].arrival_time > self.processes[i+1].arrival_time:
                        temp = self.processes[i]
                        self.processes[i] = self.processes[i+1]
                        self.processes[i+1] = temp
       
        shortest_process=[]
        
         
        for p in self.processes:
          if p.process_state==ProcessStates.READY:
              shortest_process.append(p)
        print(shortest_process[0])
        return shortest_process[0]
              
        
            
            
        
    def dispatcher_func(self, cur_process):
        
        time= self.next_event_time()-self.time 
           
        if (self.next_event_time()==float('inf')): # if the first 10 events are arrived 
                cur_process.run_for(cur_process.remaining_time ,self.time) # run the remaining process until completion 
                cur_process.process_state=ProcessStates.TERMINATED # terminate that process 
                new_event = Event(process_id=cur_process.process_id, event_time= cur_process.departure_time, event_type=EventTypes.PROC_CPU_DONE)
                return new_event
        else: # if it is  the first 10 events 
                
                cur_process.run_for(time ,self.time)# run until next event has arrived 
                if cur_process.remaining_time==0:
                    cur_process.process_state=ProcessStates.TERMINATED
                    new_event = Event(process_id=cur_process.process_id, event_time=cur_process.departure_time, event_type=EventTypes.PROC_CPU_DONE)
                    return new_event
                    
               
                else:
                    new_event = Event(process_id=cur_process.process_id, event_time= time+ self.time, event_type=EventTypes.PROC_CPU_REQ)
                    return new_event
           
            
           
            
           
            
           
            
           
            
           
            
           
            
           
