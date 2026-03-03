import { NavLink, Route, Routes } from 'react-router-dom';
import { useEffect, useState } from 'react';

const routes = ['Dashboard', 'Options', 'Stocks', 'Risk', 'Settings'] as const;

function Page({ title }: { title: string }) {
  return (
    <section className="panel">
      <h2>{title}</h2>
      <p>Step 1 scaffold in place. Feature implementation will populate this view.</p>
    </section>
  );
}

export default function App() {
  const [status, setStatus] = useState<string>('Checking API...');

  useEffect(() => {
    fetch('/api/health')
      .then((res) => res.json())
      .then((data) => setStatus(`API ${data.status} (${data.app})`))
      .catch(() => setStatus('API unreachable'));
  }, []);

  return (
    <div className="layout">
      <aside className="sidebar">
        <h1>Convexis</h1>
        <p className="muted">Self-hosted quant hedge fund ops</p>
        <nav>
          {routes.map((route) => (
            <NavLink key={route} to={route === 'Dashboard' ? '/' : `/${route.toLowerCase()}`}>
              {route}
            </NavLink>
          ))}
        </nav>
      </aside>
      <main className="content">
        <header className="topbar">
          <span>{status}</span>
        </header>
        <Routes>
          <Route path="/" element={<Page title="Dashboard" />} />
          <Route path="/options" element={<Page title="Options" />} />
          <Route path="/stocks" element={<Page title="Stocks" />} />
          <Route path="/risk" element={<Page title="Risk" />} />
          <Route path="/settings" element={<Page title="Settings" />} />
        </Routes>
      </main>
    </div>
  );
}
