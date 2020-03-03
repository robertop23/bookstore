export const state = () => ({
  books: [], // require( '@/data/books.json' ),
  drawer: false,
  links: [{
    text: 'Home',
    to: '/'
  },
  {
    text: 'About',
    href: '#about'
  },
  {
    text: 'Support',
    href: '#support'
  },
  {
    text: 'Contact',
    href: '#contact'
  }
  ]
})

export const getters = {
  isAuthenticated (state) {
    return state.auth.loggedIn
  },

  loggedInUser (state) {
    return state.auth.user
  },

  categories (state) {
    const categories = []

    for (const book of state.books) {
      if (
        !book.category ||
        categories.find(category => category.text === book.category)
      ) {
        continue
      }

      const text = book.category

      categories.push({
        text,
        to: `/category/${text}`
      })
    }
    return categories.sort().slice(0, 4)
  }

}

export const mutations = {
  setDrawer (state, payload) {
    state.drawer = payload
  },

  toggleDrawer (state) {
    state.drawer = !state.drawer
  },

  updateBooks (state, books) {
    state.books = books
  }
}

export const actions = {
  loadBooks ({
    commit
  }) {
    this.$axios.get('/books/1').then((response) => {
      this.books = response.data
      commit('updateBooks', this.books)
    })
  }
}
