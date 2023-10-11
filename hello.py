from h2o_wave import site, ui, main

# Access the web page at http://localhost:10101/
page = site['/']

# Add some content.
page['example'] = ui.markdown_card(
  box='1 1 2 2',
  title='Hello World!',
  content='And now for something completely different.',
)

# Save the page
page.save()
