"""

Template filters to partition lists into rows or columns.

A common use-case is for splitting a list into a table with columns::

    {% load partition %}
    <table>
    {% for row in mylist|columns:3 %}
        <tr>
        {% for item in row %}
            <td>{{ item }}</td>
        {% endfor %}
        </tr>
    {% endfor %}
    </table>
"""

from django.template import Library

register = Library()

def columnss(data, cols):
    rows = []
    row = []
    index = 0
    for user in data:
        row.append(user)
        index = index + 1
        if index % cols == 0:
            rows.append(row)
            row = []
    # Still stuff missing?
    if len(row) > 0:
        rows.append(row)
    return rows
    
register.filter(columnss)