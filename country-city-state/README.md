so here i have an import script for country city state 


well well



so u may imagine its like there are 3 tables country , city ,state  but no.


So here its like i created a table for each country which contains the state and then created state tables which contains cities inside them

didnt understand??? My english must be bad hahahahaha

so there are total 40k tables of countries and states !!

so why did i do this nice question!

Someone told me like bruh u have 200+ countries 4k + states and 12k + cities so by it will take more processing power when lot of people are registering so u create tables like this below

created an sql procedure which scans a table  using cursor and then using a prepared statement inside the loop i created a table based on the row name and then i used another prepared statement to insert into newly created table 

 ==>using select * from other_table where  firsttableid=other_table_foreignkeyid
 
 
 So u must be asking well yeah i got the db how do i make this work
 
 well i used this in spring boot 2.0+  with jpa repository
 
 '
 
 first query ===> select * from countries (list of all 200 countries comes)
                  assuming u get a list in ui ,u will chosen country
                  
 second query====> select * from chosen country
                          (u get a list of states)
                          
  third query=====>select * from  chosen state
                            (u will get a list of cities in that state)
                            
                            
                            
  how to use this in spring boot
  ------------------------------
  
 use jpa repository(check it on google) for first one  for doing "select * from countries" get the country u clicked and pass it to below step
 

 
 entity manager create native query(check it on the web)  to pass table name as a parameter ,jpql gave me error and doesnt allow me to pass tablename as a param
 
 eg-:   
	public default List<Object> givemethecity(String name, EntityManager e) {
		return e.createNativeQuery("SELECT city FROM "+'`'+name+'`').getResultList();
	}

}
so u got states list now

u select a state pass it to the entity manager native query  code u got cities finally select city
 
 Now  you may ask well this guy generated the tables where is the script where is it?
 
 
 
 
