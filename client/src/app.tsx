import { ReactElement } from 'react';
import { createRoot } from 'react-dom/client';

const container: HTMLElement | null = document.getElementById('root');
if (container === null) {
  throw new Error('No matching element found with ID: root');
}

const App = (): ReactElement => {
  return <h1>Hello, World!</h1>;
};

const root = createRoot(container);
root.render(<App />);