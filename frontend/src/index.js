import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import MyCharts from './MyCharts'
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
ReactDOM.render(<MyCharts />, document.getElementById('root2'));
registerServiceWorker();
