"""
Convert GitHub file links to raw content links.

This script translates GitHub web URLs to raw.githubusercontent.com URLs
for direct access to file content (useful for importing images stored on GitHub).

Examples:
    Input:  https://github.com/hyperipper/hyperipper_posts/blob/main/image.png
    Output: https://raw.githubusercontent.com/hyperipper/hyperipper_posts/main/image.png
"""

import re
import sys


def github_url_to_raw(github_url: str) -> str:
    """
    Convert a GitHub blob URL to a raw.githubusercontent.com URL.
    
    Args:
        github_url: A GitHub URL pointing to a file
        
    Returns:
        The raw.githubusercontent.com URL for the file
        
    Raises:
        ValueError: If the URL is not a valid GitHub file URL
    """
    # Pattern to match GitHub blob URLs
    pattern = r'https://github\.com/([^/]+)/([^/]+)/blob/([^/]+)/(.+)'
    match = re.match(pattern, github_url)
    
    if not match:
        raise ValueError(
            f"Invalid GitHub URL. Expected format: "
            f"https://github.com/owner/repo/blob/branch/path/to/file"
        )
    
    owner, repo, branch, filepath = match.groups()
    raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{filepath}"
    
    return raw_url


def main():
    """Main entry point for the script."""
    if len(sys.argv) != 2:
        print("Usage: python ghlink2raw.py <github-url>")
        print()
        print("Example:")
        print("  python ghlink2raw.py https://github.com/hyperipper/hyperipper_posts/blob/main/image.png")
        sys.exit(1)
    
    github_url = sys.argv[1]
    
    try:
        raw_url = github_url_to_raw(github_url)
        print(raw_url)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
