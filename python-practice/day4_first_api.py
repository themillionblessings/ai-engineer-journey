from fastapi import FastAPI, HTTPException
from typing import List, Dict, Optional
from datetime import datetime
from pydantic import BaseModel

# ═══════════════════════════════════════════════════
# DATA MODELS (Pydantic)
# ═══════════════════════════════════════════════════

class Skill(BaseModel):
    """Data model for a skill"""
    name: str
    category: str
    proficiency: int
    learned_date: str
    notes: Optional[str] = ""

class Project(BaseModel):
    """Data model for a project"""
    name: str
    description: str
    tech_stack: List[str]
    status: str
    complexity: str
    abu_dhabi_relevance: int

class DailyProgress(BaseModel):
    """Data model for daily progress"""
    day_number: int
    hours_studied: float
    topics_covered: str
    biggest_win: str
    ready_for_next: bool

# ═══════════════════════════════════════════════════
# SAMPLE DATA (In real app, this would be database)
# ═══════════════════════════════════════════════════

skills_db = [
    {
        "id": 1,
        "name": "Python Basics",
        "category": "Programming",
        "proficiency": 8,
        "learned_date": "2025-10-14",
        "notes": "Variables, functions, I/O"
    },
    {
        "id": 2,
        "name": "FastAPI",
        "category": "Web Development",
        "proficiency": 5,
        "learned_date": "2025-10-17",
        "notes": "Building APIs"
    },
    {
        "id": 3,
        "name": "SQL",
        "category": "Databases",
        "proficiency": 6,
        "learned_date": "2025-10-17",
        "notes": "Database queries"
    }
]

projects_db = [
    {
        "id": 1,
        "name": "AI Daily Motivation",
        "description": "Automated motivational emails",
        "tech_stack": ["n8n", "Gemini API", "Gmail"],
        "status": "Live",
        "complexity": "Beginner",
        "abu_dhabi_relevance": 7
    },
    {
        "id": 2,
        "name": "LinkedIn AI Generator",
        "description": "Automated LinkedIn content creation",
        "tech_stack": ["n8n", "News API", "Gemini AI", "LinkedIn API"],
        "status": "Live",
        "complexity": "Intermediate",
        "abu_dhabi_relevance": 9
    }
]

# ═══════════════════════════════════════════════════
# CREATE FASTAPI APP
# ═══════════════════════════════════════════════════

app = FastAPI(
    title="AI Learning Journey API",
    description="API for tracking AI engineering learning progress",
    version="1.0.0"
)

# ═══════════════════════════════════════════════════
# ROOT ENDPOINT
# ═══════════════════════════════════════════════════

@app.get("/")
def read_root():
    """Welcome message"""
    return {
        "message": "Welcome to AI Learning Journey API",
        "student": "Mahdi",
        "goal": "AI Engineer in Abu Dhabi",
        "current_day": 4,
        "total_days": 180,
        "status": "On Track",
        "documentation": "/docs"
    }

# ═══════════════════════════════════════════════════
# SKILLS ENDPOINTS
# ═══════════════════════════════════════════════════

@app.get("/skills")
def get_all_skills():
    """Get all skills"""
    return {
        "total": len(skills_db),
        "skills": skills_db
    }

@app.get("/skills/{skill_id}")
def get_skill(skill_id: int):
    """Get specific skill by ID"""
    skill = next((s for s in skills_db if s["id"] == skill_id), None)
    
    if skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    
    return skill

@app.get("/skills/category/{category}")
def get_skills_by_category(category: str):
    """Get skills by category"""
    filtered = [s for s in skills_db if s["category"].lower() == category.lower()]
    
    return {
        "category": category,
        "count": len(filtered),
        "skills": filtered
    }

@app.post("/skills")
def add_skill(skill: Skill):
    """Add a new skill"""
    new_id = max([s["id"] for s in skills_db]) + 1 if skills_db else 1
    
    new_skill = {
        "id": new_id,
        **skill.dict()
    }
    
    skills_db.append(new_skill)
    
    return {
        "message": "Skill added successfully",
        "skill": new_skill
    }

# ═══════════════════════════════════════════════════
# PROJECTS ENDPOINTS
# ═══════════════════════════════════════════════════

@app.get("/projects")
def get_all_projects():
    """Get all projects"""
    return {
        "total": len(projects_db),
        "projects": projects_db
    }

@app.get("/projects/{project_id}")
def get_project(project_id: int):
    """Get specific project by ID"""
    project = next((p for p in projects_db if p["id"] == project_id), None)
    
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    
    return project

@app.get("/projects/status/{status}")
def get_projects_by_status(status: str):
    """Get projects by status"""
    filtered = [p for p in projects_db if p["status"].lower() == status.lower()]
    
    return {
        "status": status,
        "count": len(filtered),
        "projects": filtered
    }

# ═══════════════════════════════════════════════════
# STATISTICS ENDPOINTS
# ═══════════════════════════════════════════════════

@app.get("/stats")
def get_statistics():
    """Get learning statistics"""
    
    # Skills stats
    total_skills = len(skills_db)
    avg_proficiency = sum(s["proficiency"] for s in skills_db) / total_skills if total_skills > 0 else 0
    
    # Projects stats
    total_projects = len(projects_db)
    live_projects = len([p for p in projects_db if p["status"] == "Live"])
    avg_relevance = sum(p["abu_dhabi_relevance"] for p in projects_db) / total_projects if total_projects > 0 else 0
    
    return {
        "journey": {
            "current_day": 4,
            "total_days": 180,
            "progress_percentage": (4 / 180) * 100
        },
        "skills": {
            "total": total_skills,
            "average_proficiency": round(avg_proficiency, 1)
        },
        "projects": {
            "total": total_projects,
            "live": live_projects,
            "average_abu_dhabi_relevance": round(avg_relevance, 1)
        }
    }

@app.get("/stats/progress")
def get_progress():
    """Get detailed progress report"""
    days_completed = 4
    days_remaining = 180 - days_completed
    estimated_hours = days_completed * 4  # Assuming 4 hours/day
    
    return {
        "timeline": {
            "start_date": "2025-10-14",
            "current_day": days_completed,
            "days_remaining": days_remaining,
            "percentage_complete": round((days_completed / 180) * 100, 2),
            "estimated_completion": "2026-04-12"
        },
        "effort": {
            "total_hours": estimated_hours,
            "average_hours_per_day": 4.0,
            "projected_total_hours": 180 * 4
        },
        "milestones": {
            "skills_learned": len(skills_db),
            "projects_built": len(projects_db),
            "github_commits": 4
        },
        "status": "On Track ✅"
    }

# ═══════════════════════════════════════════════════
# HEALTH CHECK
# ═══════════════════════════════════════════════════

@app.get("/health")
def health_check():
    """API health check"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }

# ═══════════════════════════════════════════════════
