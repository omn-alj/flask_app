from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Placeholder list for storing blog posts (replace with your own data source)
blog_posts = []

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # Create a new blog post object or store it in a database
        post = {
            'title': title,
            'content': content
        }
        blog_posts.append(post)  # Add the new post to the list
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # Update the blog post with the given post_id (implement your own logic)
        for post in blog_posts:
            if post['post_id'] == post_id:
                post['title'] = title
                post['content'] = content
                break
        return redirect(url_for('index'))
    # Fetch the blog post data and pass it to the update.html template
    for post in blog_posts:
        if post['post_id'] == post_id:
            return render_template('update.html', post=post)
    return "Post not found", 404

@app.route('/delete/<int:post_id>')
def delete(post_id):
    # Delete the blog post with the given post_id (implement your own logic)
    for post in blog_posts:
        if post['post_id'] == post_id:
            blog_posts.remove(post)
            break
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html', blog_posts=blog_posts)

# Run the Flask application
if __name__ == '__main__':
    app.run()
