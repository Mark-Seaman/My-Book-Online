#!/usr/bin/env python
# Create a structured list for the menu

from sys        import argv
from json       import dumps,loads
from os.path    import exists, dirname
from os         import chdir
from json import dumps

#-----------------------------------------------------------------------------
# Readers
#-----------------------------------------------------------------------------

# Scan the menu and remove bad items
def fix_menu(path, menu):
    results = []
    for item in menu.split('\n'):
        x = item.split(',')
        if len(x) > 4:
            print 'BAD: ', item
            item = ','.join([ '%s %s'%(x[0],x[1]), x[2], x[3], x[4] ])
        results.append(item)
    f = open(path,'w')
    f.write('\n'.join(results))
    f.close()

# Pull apart the item into its components
def frack(item):
    x = item.split(',')
    if len(x)<4: 
        return
    if len(x[3]) == 0:
        x[3]=x[4]
    if len(x)!=5:
        return
    return x

# Add the menu item to the data structure
def add_menu_item(menu, item):
    x = frack(item)
    if x:
        id,name,price,group,category = x
        selection = { 'name':x[0]+x[1]+x[2]+','+x[3], 'price':price, 'parts':x }
    
        if menu.has_key(category):
            if menu[category].has_key(group):
                menu[category][group].append(selection)
            else:
                menu[category][group] = [ selection ]
        else:
            menu[category] = { group: [ selection ] }
        return menu

    
def create_menu(menu_text):
    id = 0
    menu = {}
    for item in menu_text.split('\n'):
        id += 1
        if len(item)>10:
            menu = add_menu_item(menu, '%d,'%id+item) 
    return  menu

#-----------------------------------------------------------------------------
# Writers
#-----------------------------------------------------------------------------

# Print out the json for the menu
def print_menu_json(menu):
    print  dumps(menu)


# Print out the menu in text format
def print_menu_text(menu):
    print "Today's menu"
    for m in sorted(menu):
        print '\n.......................\n\n',m
        for group in menu[m]:
            print '\n    ', group
            for item in menu[m][group]:
                print '        ', item['parts'][1], '...', '$%s'%item['parts'][2]


ctrl_begin   = '<form id="main" ng-controller="food_selector">'
ctrl_end     = '</form>'

page_begin   = '''<h1>%s</h1>
    <a href="Index">Index</a> * 
    <a href='Select'>Select Food</a> * 
    <a href="Summary">Summary</a><br><br>'''
page_end     = ''

tabset_begin = '<tabset ng-show="true">\n'
tabset_end   = '</tabset>\n'

group_begin  = '<tab heading="%s"><div class="page"><ul>\n'
group_end    = '</ul></div></tab>\n'

# Print the controls for a single menu item
def print_item_raw(item):
    id,name,price,group,category = item
    print """
        <li><label>
            <span>%s, $%s (%s,%s)</span>
        </label></li>
    """%(name,price,group,category)


# Print the controls for a single menu item
def print_item_select(item):
    id,name,price,group,category = item
    print """
        <li><label>
            <input type='checkbox' ng-click='select_item(%s,"%s",%s)'>
            <span>%s, $%s (%s,%s)</span>
        </label></li>
    """%(id,name,price,name,price,group,category)


# Print a list of all items in all category
def print_menu_html(menu,print_item=print_item_raw):
    for m in sorted(menu):
        print group_begin%m
        for group in menu[m]:
            print '\n<br><b>%s</b>'%group
            print '<ul class="unstyled">'

            for item in menu[m][group]:
               print_item(item['parts'])

            print '</ul><br>\n'
        print group_end


# Show the html for the menu selector
def print_selector_html(menu):
    print_menu_html(menu,print_item_select)


# Print summary in HTML
def print_summary_page():
    print '''
      <div class='page'>
        <b>Your Selections</b>
        <ul id="selected">
          <li ng-repeat="i in selected">
            <label>{{i}}</label>
          </li>
        </ul> 
        <p id="total">total cost: <span>${{total()}}</span></p>
      </div>     
      <input type="submit" id="save" value="Save"/>
    ''' 
#          <li ng-repeat="i in selected()">
#            <label>{{i.name}}</label>


# Print selector in HTML
def print_selector_page(menu):
    print ctrl_begin
    print page_begin%"Summary"

    #print_menu_json(menu)
    print_summary_page()

    #print '<pre>{{ menuItems() }}</pre>'
    print '<pre>{{ menutxt }}</pre>'

    print tabset_begin

    print_selector_html(menu)

    print tabset_end

    print page_end
    print ctrl_end


#-----------------------------------------------------------------------------
# Top level script

# Print the food data with the selected treatment
def print_menu_file(path, format=print_menu_text):
    if not exists(path):
        print 'No file found,',path
        exit(1)
    else:
        menu_text = open(path).read()
        menu = create_menu(menu_text)
        format(menu)


