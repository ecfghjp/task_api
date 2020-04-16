db.auth('admin', 'admin')
db.createUser(
    {
        user: "task_ecfghjp",
        pwd: "task_ecfghjp",
        roles: [
            {
                role: "readWrite",
                db: "tasks"
            }
        ]
    }
);
