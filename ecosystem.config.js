// ==============================================================================
// ENTERPRISE PROCESS MANAGEMENT CONTROLLER: DAMODAR TECHCRAZE VENTURES
// FILE PATH: ecosystem.config.js | ZERO MONITORING SYSTEM MAINTENANCE
// ==============================================================================

module.exports = {
  apps: [
    {
      name: 'Damodar-Core-Gateway',
      script: './server.js',
      instances: 1,
      autorestart: true,
      watch: false,
      env: {
        NODE_ENV: 'development',
        PORT: 8080
      }
    },
    {
      name: 'Damodar-Lead-Harvester',
      script: './daemons/lead_harvester.py',
      interpreter: 'python3',
      instances: 1,
      autorestart: true,
      watch: false
    },
    {
      name: 'Damodar-Video-Factory',
      script: './daemons/video_factory.py',
      interpreter: 'python3',
      instances: 1,
      autorestart: true,
      watch: false
    }
  ]
};