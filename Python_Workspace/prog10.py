#dictionary inside dictionary
college_dict = {
    'Dev Bhomi' : {
      'Sameer' : {
          'Last-Name' : 'Ansari',
          'Year' : 1,
          'Course' : {
              'Course' : 'Btech',
              'Fav-Subject' : 'HTML'
          }
      }
    },
    'Graphic Era': {
        'Nikita' : {
            'Last-Name' : 'Pundir',
            'Year' : 2,
            'Course' : {
                'Course' : 'Btech',
                'Fav-Subject' : 'Javascript'
            }
        }
    },
    'DIT': {
        'Prachi' : {
            'Last-Name' : 'Pant',
            'Year' : 3,
            'Course' : {
                'Course' : 'Btech',
                'Fav-Subject' : 'Ajax'
            }
        }
    }
}

# access dictionary
print college_dict['Graphic Era']['Nikita']['Course']['Fav-Subject']
# keys in a dictionary
print college_dict['Graphic Era'].keys()
# number of keys inside dictionary
print len(college_dict['Graphic Era'].keys())
# modify dictionary
print college_dict['Graphic Era']['Nikita']['Year']
college_dict['Graphic Era']['Nikita']['Year']=10
print college_dict['Graphic Era']['Nikita']['Year']

college_dict['Graphic Era']['Nikita']['Course']['Fav_subject'] = 'Rocket Science'
print college_dict['Graphic Era']['Nikita']['Course']['Fav_subject']
college_dict['Graphic Era']['Nikita']['Course'] = 'Mtech'
print college_dict['Graphic Era']['Nikita']['Course']

# Add new entery in dictionary
college_dict['Graphic Era'].update({
    'Abhishek' : {
        'Last_Name' : 'Parmar',
        'Year' : 9,
        'Course' : {
            'Course' : 'Mtech',
            'Fav-Subject' : 'OS'
        }
    }
})

#print new element
print college_dict['Graphic Era']['Abhishek']['Course']['Fav-Subject']

print college_dict['Graphic Era'].keys()

del college_dict['Graphic Era']['Abhishek']
print college_dict['Graphic Era'].keys()