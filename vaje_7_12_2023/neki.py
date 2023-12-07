import sqlite3
import os

conn =sqlite3.connect("vaje_7_12_2023\\filmi.sqlite")
rezultat=conn.execute("select naslov,dolzina from film")
#print(rezultat.fetchone())
#for vrstica in rezultat:
#    print(vrstica)
rezultat.close()
rez=conn.execute("select naslov,ocena from film order by ocena DESC limit 20;")
#for vr in rez:
    #print(vr)
rez.close()

#tretja
rez=conn.execute("select oznaka, count(*) from film group by oznaka")

#for vr in rez :
#    print(vr)
    
rez.close()
#cetrta

conn.close()

conn =sqlite3.connect("vaje_7_12_2023\\svet.sqlite")
kazalec=conn.cursor()

kazalec.execute(""" DROP TABLE IF EXISTS kontinent;""")

kazalec.execute("""
    create table kontinent(
    id integer PRIMARY KEY,
    ime text NOT NULL);            
""")

kazalec.execute(""" DROP TABLE IF EXISTS drzava;""")

kazalec.execute(""" 
    create table drzava(
    id integer PRIMARY KEY,
    ime text NOT NULL,
    povrsina float CHECK(povrsina > 0),  
    id_kontinenta integer references kontinent(id)  
    );                
                
""")
kazalec.execute(
    """
    INSERT INTO kontinent(ime)
    values("europa");
    """ 
)

try:
    with conn:
        kazalec.execute(
            """
            INSERT INTO drzava(ime,povrsina,id_kontinenta)
            values("slo",3, (SELECT id from kontinent where ime="europa"));
            """ 
    )
except sqlite3.IntegrityError as x:
    print(x )   

conn.commit()

kazalec.close()
conn.close()



"""
try:    
    with conn
    kazalec.execute......
    poizvedve
exept sqlite3.integrityError as x:
    print(napaka )



in potem ne rabiš vec comit 
    
"""