def check_progress(day, skills_learned, projects_built):
    """Evaluate your learning progress"""
    
    # Calculate progress percentage
    total_days = 180
    progress_percent = (day / total_days) * 100
    
    # Check if on track
    expected_skills = day * 0.5  # Should learn ~0.5 skills per day
    expected_projects = day / 7   # Should complete ~1 project per week
    
    print(f"\n{'='*50}")
    print(f"PROGRESS REPORT - DAY {day}")
    print(f"{'='*50}")
    print(f"Overall Progress: {progress_percent:.1f}%")
    print(f"Skills Learned: {skills_learned} (Expected: {expected_skills:.0f})")
    print(f"Projects Built: {projects_built} (Expected: {expected_projects:.0f})")
    
    # Evaluate performance
    if skills_learned >= expected_skills and projects_built >= expected_projects:
        status = "🚀 AHEAD OF SCHEDULE!"
        advice = "Keep this momentum! You're crushing it!"
    elif skills_learned >= expected_skills * 0.8:
        status = "✅ ON TRACK"
        advice = "Great progress! Stay consistent!"
    else:
        status = "⚠️ NEEDS ATTENTION"
        advice = "Spend more time on hands-on practice."
    
    print(f"\nStatus: {status}")
    print(f"Advice: {advice}")
    print(f"{'='*50}\n")

# Test with your actual Day 2 progress: 2 days elapsed, 7 skills, 2 projects (including the motivation system)
check_progress(2, 7, 2)
