# Write a query that will display the results below (Note: some columns might be renamed
# but use the column names above). It should only show 2020 data and order by driver
# points.


query= """  
SELECT 
        drivers.driver_name, 
        results.points, 
        races.race_name
    FROM 
        drivers
    INNER JOIN 
        results ON drivers.driver_id = results.driver_id
    INNER JOIN 
        races ON results.race_id = races.race_id
    WHERE 
        races.year = 2020
    ORDER BY 
        results.points DESC;
        
        """