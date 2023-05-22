# Initial loads
from src import db,app
from src.models.book import Book
from src.models.section import Section
from src.models.page import Page
import random


book_initial_load = [
    {
        "id": 1,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1586722975i/2767052._S50_.jpg",
        "title": "The Hunger Games (The Hunger Games, #1)"
    },
    {
        "id": 2,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1546910265i/2._S75_.jpg",
        "title": "Harry Potter and the Order of the Phoenix (Harry Potter, #5)"
    },
    {
        "id": 3,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320399351i/1885._S75_.jpg",
        "title": "Pride and Prejudice"
    },
    {
        "id": 4,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1553383690i/2657._S75_.jpg",
        "title": "To Kill a Mockingbird"
    },
    {
        "id": 5,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1522157426i/19063._S75_.jpg",
        "title": "The Book Thief"
    },
    {
        "id": 6,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1361039443i/41865._S75_.jpg",
        "title": "Twilight (The Twilight Saga, #1)"
    },
    {
        "id": 7,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1325861570i/170448._S75_.jpg",
        "title": "Animal Farm"
    },
    {
        "id": 8,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1656625315i/30._S50_.jpg",
        "title": "J.R.R. Tolkien 4-Book Boxed Set: The Hobbit and The Lord of the Rings"
    },
    {
        "id": 9,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1661032875i/11127._S75_.jpg",
        "title": "The Chronicles of Narnia (Chronicles of Narnia, #1-7)"
    },
    {
        "id": 10,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1660273739i/11870085._S50_.jpg",
        "title": "The Fault in Our Stars"
    },
    {
        "id": 11,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1551144577i/18405._S75_.jpg",
        "title": "Gone with the Wind"
    },
    {
        "id": 12,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1174210942i/370493._S50_.jpg",
        "title": "The Giving Tree"
    },
    {
        "id": 13,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1546103428i/5297._S75_.jpg",
        "title": "The Picture of Dorian Gray"
    },
    {
        "id": 14,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388212715i/6185._S75_.jpg",
        "title": "Wuthering Heights"
    },
    {
        "id": 15,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1170803558l/72193._S50_SY75_.jpg",
        "title": "Harry Potter and the Philosopher’s Stone (Harry Potter, #1)"
    },
    {
        "id": 16,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1557343311i/10210._S75_.jpg",
        "title": "Jane Eyre"
    },
    {
        "id": 17,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1650033115i/22628._S50_.jpg",
        "title": "The Perks of Being a Wallflower"
    },
    {
        "id": 18,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1579621267i/968._S75_.jpg",
        "title": "The Da Vinci Code (Robert Langdon, #2)"
    },
    {
        "id": 19,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1490528560i/4671._S75_.jpg",
        "title": "The Great Gatsby"
    },
    {
        "id": 20,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1630487234i/24213._S50_.jpg",
        "title": "Alice's Adventures in Wonderland / Through the Looking-Glass"
    },
    {
        "id": 21,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1367545443i/157993._S75_.jpg",
        "title": "The Little Prince"
    },
    {
        "id": 22,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1409595968i/929._S75_.jpg",
        "title": "Memoirs of a Geisha"
    },
    {
        "id": 23,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1400602609i/28187._S75_.jpg",
        "title": "The Lightning Thief (Percy Jackson and the Olympians, #1)"
    },
    {
        "id": 24,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1618526890i/13335037._S75_.jpg",
        "title": "Divergent (Divergent, #1)"
    },
    {
        "id": 25,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1411852091i/24280._S75_.jpg",
        "title": "Les Misérables"
    },
    {
        "id": 26,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1382846449i/7144._S75_.jpg",
        "title": "Crime and Punishment"
    },
    {
        "id": 27,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327869409i/7624._S75_.jpg",
        "title": "Lord of the Flies"
    },
    {
        "id": 28,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1629680008i/18135._S75_.jpg",
        "title": "Romeo and Juliet"
    },
    {
        "id": 29,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1615094578i/8127._S75_.jpg",
        "title": "Anne of Green Gables (Anne of Green Gables, #1)"
    },
    {
        "id": 30,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1432730315i/256683._S75_.jpg",
        "title": "City of Bones (The Mortal Instruments, #1)"
    },
    {
        "id": 31,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1559986152l/386162._S50_SY75_.jpg",
        "title": "The Hitchhiker's Guide to the Galaxy (The Hitchhiker's Guide to the Galaxy, #1)"
    },
    {
        "id": 32,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1622355533i/4667024._S75_.jpg",
        "title": "The Help"
    },
    {
        "id": 33,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1408303130i/375802._S75_.jpg",
        "title": "Ender’s Game (Ender's Saga, #1)"
    },
    {
        "id": 34,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1628267712i/24178._S75_.jpg",
        "title": "Charlotte's Web"
    },
    {
        "id": 35,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1387151694i/17245._S75_.jpg",
        "title": "Dracula"
    },
    {
        "id": 36,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1511302904i/890._S50_.jpg",
        "title": "Of Mice and Men"
    },
    {
        "id": 37,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1654371463i/18144590._S75_.jpg",
        "title": "The Alchemist"
    },
    {
        "id": 38,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1398034300i/5107._S75_.jpg",
        "title": "The Catcher in the Rye"
    },
    {
        "id": 39,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1575509280i/5129._S75_.jpg",
        "title": "Brave New World"
    },
    {
        "id": 40,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327881361i/320._S50_.jpg",
        "title": "One Hundred Years of Solitude"
    },
    {
        "id": 41,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1383718290i/13079982._S75_.jpg",
        "title": "Fahrenheit 451"
    },
    {
        "id": 42,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1380660571i/18619684._S50_.jpg",
        "title": "The Time Traveler's Wife"
    },
    {
        "id": 43,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1655336738i/128029._S75_.jpg",
        "title": "A Thousand Splendid Suns"
    },
    {
        "id": 44,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327903636i/21787._S75_.jpg",
        "title": "The Princess Bride"
    },
    {
        "id": 45,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327873635i/2998._S75_.jpg",
        "title": "The Secret Garden"
    },
    {
        "id": 46,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1562726234i/13496._S75_.jpg",
        "title": "A Game of Thrones (A Song of Ice and Fire, #1)"
    },
    {
        "id": 47,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1442129426i/231804._S75_.jpg",
        "title": "The Outsiders"
    },
    {
        "id": 48,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1507963312i/33574273._S50_.jpg",
        "title": "A Wrinkle in Time (Time Quintet, #1)"
    },
    {
        "id": 49,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1390173285i/1381._S75_.jpg",
        "title": "The Odyssey"
    },
    {
        "id": 50,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1562690475i/1934._S75_.jpg",
        "title": "Little Women"
    },
    {
        "id": 51,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1532714506i/40961427._S50_.jpg",
        "title": "1984"
    },
    {
        "id": 52,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1546096879i/2956._S50_.jpg",
        "title": "The Adventures of Huckleberry Finn"
    },
    {
        "id": 53,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1457810586i/12232938._S75_.jpg",
        "title": "The Lovely Bones"
    },
    {
        "id": 54,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1579036753i/77203._S75_.jpg",
        "title": "The Kite Runner"
    },
    {
        "id": 55,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1384434560i/19543._S50_.jpg",
        "title": "Where the Wild Things Are"
    },
    {
        "id": 56,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1631088473i/35031085._S75_.jpg",
        "title": "Frankenstein: The 1818 Text"
    },
    {
        "id": 57,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1673212751i/23772._S50_.jpg",
        "title": "Green Eggs and Ham"
    },
    {
        "id": 58,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1631251689i/4214._S75_.jpg",
        "title": "Life of Pi"
    },
    {
        "id": 59,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1344922523i/1953._S75_.jpg",
        "title": "A Tale of Two Cities"
    },
    {
        "id": 60,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1578028274i/38447._S75_.jpg",
        "title": "The Handmaid’s Tale (The Handmaid's Tale, #1)"
    },
    {
        "id": 61,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1663805647i/136251._S75_.jpg",
        "title": "Harry Potter and the Deathly Hallows (Harry Potter, #7)"
    },
    {
        "id": 62,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1342493368i/3636._S75_.jpg",
        "title": "The Giver (The Giver, #1)"
    },
    {
        "id": 63,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1377756377i/7604._S75_.jpg",
        "title": "Lolita"
    },
    {
        "id": 64,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1667708346i/43641._S75_.jpg",
        "title": "Water for Elephants"
    },
    {
        "id": 65,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1440319389i/4981._S75_.jpg",
        "title": "Slaughterhouse-Five"
    },
    {
        "id": 66,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1555447414i/44767458._S75_.jpg",
        "title": "Dune (Dune, #1)"
    },
    {
        "id": 67,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1630547330i/5._S75_.jpg",
        "title": "Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)"
    },
    {
        "id": 68,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1213131305i/149267._S50_.jpg",
        "title": "The Stand"
    },
    {
        "id": 69,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1463157317i/168668._S75_.jpg",
        "title": "Catch-22"
    },
    {
        "id": 70,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1554582218i/6514._S75_.jpg",
        "title": "The Bell Jar"
    },
    {
        "id": 71,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388793265i/39988._S75_.jpg",
        "title": "Matilda"
    },
    {
        "id": 72,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1576956100i/5043._S75_.jpg",
        "title": "The Pillars of the Earth (Kingsbridge, #1)"
    },
    {
        "id": 73,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1164045516i/3590._S75_.jpg",
        "title": "The Adventures of Sherlock Holmes (Sherlock Holmes, #3)"
    },
    {
        "id": 74,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1405136931i/76620._S75_.jpg",
        "title": "Watership Down (Watership Down, #1)"
    },
    {
        "id": 75,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1631687432i/2623._S75_.jpg",
        "title": "Great Expectations"
    },
    {
        "id": 76,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1386605169i/17899948._S50_.jpg",
        "title": "Rebecca"
    },
    {
        "id": 77,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1684638853i/2429135._S50_.jpg",
        "title": "The Girl with the Dragon Tattoo (Millennium, #1)"
    },
    {
        "id": 78,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1659086907i/10964._S75_.jpg",
        "title": "Outlander (Outlander, #1)"
    },
    {
        "id": 79,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1516211014i/332613._S50_.jpg",
        "title": "One Flew Over the Cuckoo's Nest"
    },
    {
        "id": 80,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1572261616l/52892857._S50_SY75_.jpg",
        "title": "The Color Purple"
    },
    {
        "id": 81,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1369504683i/10917._S75_.jpg",
        "title": "My Sister's Keeper"
    },
    {
        "id": 82,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1654215925i/61215351._S75_.jpg",
        "title": "The Fellowship of the Ring (The Lord of the Rings, #1)"
    },
    {
        "id": 83,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1601352433i/15823480._S50_.jpg",
        "title": "Anna Karenina"
    },
    {
        "id": 84,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1427728126i/4934._S50_.jpg",
        "title": "The Brothers Karamazov"
    },
    {
        "id": 85,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327883484i/14891._S75_.jpg",
        "title": "A Tree Grows in Brooklyn"
    },
    {
        "id": 86,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1549260060i/41817486._S50_.jpg",
        "title": "A Clockwork Orange"
    },
    {
        "id": 87,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1600241424i/6288._S75_.jpg",
        "title": "The Road"
    },
    {
        "id": 88,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348317139i/252577._S75_.jpg",
        "title": "Angela's Ashes (Frank McCourt, #1)"
    },
    {
        "id": 89,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1361098973i/345627._S75_.jpg",
        "title": "Vampire Academy (Vampire Academy, #1)"
    },
    {
        "id": 90,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1629378189i/52036._S75_.jpg",
        "title": "Siddhartha"
    },
    {
        "id": 91,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1505766203i/119322._S50_.jpg",
        "title": "The Golden Compass (His Dark Materials, #1)"
    },
    {
        "id": 92,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1638425885i/16299._S75_.jpg",
        "title": "And Then There Were None"
    },
    {
        "id": 93,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1334416842i/830502._S75_.jpg",
        "title": "It"
    },
    {
        "id": 94,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1554368352i/2654._S50_.jpg",
        "title": "To Kill a Mockingbird"
    },
    {
        "id": 95,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327942676i/23919._S75_.jpg",
        "title": "The Complete Stories and Poems"
    },
    {
        "id": 96,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1353277730i/11588._S75_.jpg",
        "title": "The Shining (The Shining, #1)"
    },
    {
        "id": 97,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1644073807i/7244._S75_.jpg",
        "title": "The Poisonwood Bible"
    },
    {
        "id": 98,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1380631642i/43763._S75_.jpg",
        "title": "Interview with the Vampire (The Vampire Chronicles, #1)"
    },
    {
        "id": 99,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1546112331i/3836._S50_.jpg",
        "title": "Don Quixote"
    },
    {
        "id": 100,
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1329189714i/2165._S75_.jpg",
        "title": "The Old Man and the Sea"
    }
]

def run_initial_load():
    try:
        sections =[]
        books = []
        pages = []
        section_idx = 1
        page_idx = 1
        #Insert books 
        for current_book in book_initial_load:
            books.append(
                Book(
                    id = current_book['id'],
                    cover_image = current_book['cover'],
                    name = current_book['title'],
                    description = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry`s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum'    
                )
            )
            #Insert Sections
            for current_book_section_idx in range(5):
                section_idx = section_idx + 1
                sections.append(
                    Section(
                        id = section_idx,
                        book_id = current_book['id'],
                        heading = 'section {} from book {} '.format(current_book['id' ],current_book['title']),
                        parent_section = ' parent section from book {}'.format(current_book['title'])
                    )
                )
                # Insert pages
                for current_book_page_idx in range(10):
                    page_idx = page_idx + 1
                    pages.append(
                        Page(
                            id=page_idx,
                            content = ' Page {} from section {} from section Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry`s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum'.format(page_idx,section_idx),
                            page_number = current_book_page_idx,
                            section_id =  section_idx
                        )
                    )
        
        db.session.bulk_save_objects(books)
        db.session.bulk_save_objects(sections)
        db.session.bulk_save_objects(pages)
        db.session.commit()
        
    except Exception as e:
        app.logger.error(e)
        
    return 
