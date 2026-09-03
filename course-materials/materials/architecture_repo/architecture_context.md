# Repository Architecture Context

The ordering service uses the following approved boundaries:

- domain functions receive policy as data and remain deterministic;
- environment variables are read only in the application composition layer;
- reusable input validation belongs in `pricing.validation`;
- domain modules do not create mutable process-global caches;
- local tests use synthetic configuration and never require production secrets;
- a merge decision must consider behavior, coupling, security, operability,
  rollback, and remaining uncertainty.

Treat these as existing repository constraints. Determine compliance from code
and reproducible evidence rather than from candidate descriptions.
