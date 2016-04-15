#!/usr/bin/python
# -*-coding: utf-8 -*-
#


def _createTOPfile_0():
	""" """
	print 'Excuse me ! Hello ?!'
  	csv_ru = csv_to_list('/Users/max/Downloads/FPP.csv')
        print csv_ru
	for row in range(len(csv_ru)):
		print row



print "Helloy ?!"	
_createTOPfile_0()


"""
	var rates_t8 = SpreadsheetApp.open(file);
  data =  rates_t8.getDataRange().getValues();
  Logger.log(data.length);
  
  def_find = []
  for (i = 9; i < (data.length) - 5; i++){
    if (data[i][0].length <= 5) {
      def_find.push(data[i])
      }
    
  }
  Logger.log(def_find.length);
  // rand from 85 
  
  var random_def_top = []
  var rn = 1
  var def_final_range = [];
  
for (k = 1; k < 10;k++){ 
 def_final_range[k] = []
  for (j in def_find){
    if (def_find[j][0][0]==k) {
      def_final_range[k].push(def_find[j]);
      }
    }
  
  }
  
  var sum_defs = 0;
  for (m = 1 ; m < 10 ;m ++) {
    counter_country_defs.push(def_final_range[m].length);
    sum_defs =+  counter_country_defs[m]
    // here 217 
    
  }
  
  while (sum_defs > 81) {
    for (m = 1 ; m < 10 ;m ++) {
     if (counter_country_defs[m] > 81 || sum_defs > 81)
        Logger.log(sum_defs) 
        counter_country_defs[m] = counter_country_defs[m] - 1;
        sum_defs =+  counter_country_defs[m]
  }
  }
   Logger.log('*****------****')
  Logger.log(counter_country_defs)
  }
 /*
  
  // 0,0,4,0,0,0,212,0,1 counter_country_defs
 for (m = 1; m < 10; m++){
   while (sum_defs < 81){
   
   
   if (counter_country_defs[m] > 0){
   
   sum_def++;
   }
   
   } 
     
   
   }
 }
 while (sum_defs == 81){
 
     counter_country_defs[m]
   }
   
 }
 while (def_final_range.length < 82){
 // if counter_country_defs
 }
 
}
*/


function _RandUniqueArray_FromArray(array_defs) {

var arr = []
var range  = array_defs.length
while(arr.length < 9){
  var randomnumber=Math.ceil(Math.random()*range)
  var found=false;
  for(var i=0;i<arr.length;i++){
	if(arr[i]==randomnumber){found=true;break}
  }
  if(!found)arr[arr.length]=randomnumber;
}
var arr0 = []
for (i in arr){
  arr0.push(arr[i])
}
return arr0

}
"""


