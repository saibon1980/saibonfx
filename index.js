import React, { Component } from 'react';
import { render } from 'react-dom';
import Hello from './Hello';
import './style.css';

class App extends Component {
  constructor() {
    super();
    this.state = {
      name: 'React'
    };
  }

  render() {
    return (
      <div>
        <Hello name={this.state.name} />
        <p>
          Research and development of algorithms to help recognize market place trends, reversals, patterns, and divergences across all asset groups.
        </p>
      </div>
    );
  }
}

render(<App />, document.getElementById('root'));
