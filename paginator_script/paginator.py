class Paginator:

    objects = []
    items_per_page = 0
    pages = []

    def __init__ (self, objects, items_per_page):
        self.objects = objects
        self.items_per_page = items_per_page
        self.set_pages()
    
    # Set pages accordingly
    def set_pages(self):
        objects_for_page = []
        for object in range(0, len(self.objects), self.items_per_page ):
            objects_for_page.append(self.objects[object:object+self.items_per_page])

        for index, object in enumerate(objects_for_page, start=1):
            page_number = index 
            total_page_number = len(objects_for_page)
            has_next_condition = True
            has_previous_condition = True
            if (index == 1):
                has_previous_condition = False
            if (index == len(objects_for_page)):
                has_next_condition = False
            page = Page(object, page_number, total_page_number, has_next_condition, has_previous_condition)
            self.pages.append(page)
    

    # Display number of objects in the list
    def count(self):
        print(len(self.objects))
    
    # Display number of pages according to the list
    def num_pages(self):
        print(len(self.pages))
    
    # Return the page according to the number specified
    def page(self, number):
        for index, page in enumerate(self.pages, start=1):
            if (index == number):
                return page



class Page:

    objects =[]
    page_number = 0
    total_page_number = 0
    has_next_condition = True
    has_previous_condition = True

    def __init__(self, objects, page_number, total_page_number, has_next_condition, has_previous_condition):
        self.objects = objects
        self.page_number = page_number
        self.total_page_number = total_page_number
        self.has_next_condition = has_next_condition
        self.has_previous_condition = has_previous_condition
    
    def object_list(self):
        return self.objects

    def has_next(self):
        return self.has_next_condition
    
    def has_previous(self):
        return self.has_previous_condition

    def __str__ (self):
        return f"<Page {self.page_number} of {self.total_page_number}>"
    
# Test function
def main():
    objects = [
        "Lauren Vickers",
        "Shazia Darby",
        "Zara Cain",
        "Edna Bradbury Parsons",
        "Clair Newton",
        "April Bruce Cain Kieran",
        "Timothy Bower",
        "Tracie Atkin Stanton",
        "Mabel Meadows",
        "Helen Rolfe",
        "Catriona Sampson"
    ]
    items_per_page = 3

    paginator = Paginator(objects, items_per_page)
    paginator.count()
    paginator.num_pages()

    page1 = paginator.page(1)
    print(page1)
    print(page1.object_list())
    print(page1.has_next())
    print(page1.has_previous())

    page4 = paginator.page(2)
    print(page4)
    print(page4.object_list())
    print(page4.has_next())
    print(page4.has_previous())

    page4 = paginator.page(3)
    print(page4)
    print(page4.object_list())
    print(page4.has_next())
    print(page4.has_previous())

    page4 = paginator.page(4)
    print(page4)
    print(page4.object_list())
    print(page4.has_next())
    print(page4.has_previous())




if __name__ == "__main__":
    main()
    




